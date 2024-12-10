import asyncio
from uuid import UUID

import pandas as pd
from fastapi import UploadFile
from pydantic import ValidationError

from app.factories.file_processor_factory import ProcessorFactory
from app.factories.payment_provider_factory import PaymentFactory
from app.helpers.constants import (
    FAKE_SMTP_PASS,
    FAKE_SMTP_PORT,
    FAKE_SMTP_SERVER,
    FAKE_SMTP_USERNAME,
    PAYMENT_CONFIRMATION_SUBJECT,
)
from app.helpers.providers import get_providers
from app.interfaces.handlers import APIHandler
from app.schemas.debt import CustomerDebt
from app.services.email.email_service import SMTPEmailEngine
from app.services.email.template_service import template_service


class PaymentHandler(APIHandler):

    async def get_content(self, customer_name: str, debt_id: UUID):
        content = template_service.render_template(
            template_name=template_service.payment_confirmation_template,
            context={"customer_name": customer_name, "debt_id": str(debt_id)},
        )
        if not content:
            raise ValidationError("Error while rendering template")
        return content

    async def process_payment_task(self, row, mail_server: SMTPEmailEngine):
        customer_debt = CustomerDebt(  # Lavaraging pydantic validation
            customer_name=row.get("name"),
            debt_id=row.get("debtId"),
            email=row.get("email"),
            amount=row.get("debtAmount"),
        )
        provider = get_providers()
        payment_provider = PaymentFactory.get_payment_service(provider)
        await payment_provider.process_payment(customer_debt=customer_debt)
        mail_server.send_email(
            to=customer_debt.email,
            subject=PAYMENT_CONFIRMATION_SUBJECT,
            html=await self.get_content(
                customer_name=customer_debt.customer_name, debt_id=customer_debt.debt_id
            ),
        )

    async def get_result(self, file: UploadFile):
        file_service = ProcessorFactory.get_processor(file=file)
        tasks = []
        with SMTPEmailEngine(
            smtp_port=FAKE_SMTP_PORT,
            smtp_server=FAKE_SMTP_SERVER,
            username=FAKE_SMTP_USERNAME,
            password=FAKE_SMTP_PASS,
        ) as mail_server:
            for chunk in file_service.process_file(file):
                try:
                    if isinstance(chunk, pd.DataFrame):
                        for _, row in chunk.iterrows():
                            tasks.append(
                                self.process_payment_task(
                                    row=row, mail_server=mail_server
                                )
                            )
                except ValidationError as e:
                    # Add DLQ so that we capture failed data to reprocess if needed.
                    print("Error while parsing data")
                    raise e
                except Exception as er:
                    # Add DLQ so that we capture failed data to reprocess if needed.
                    print("Error while processing data")
                    raise er
                else:
                    await asyncio.gather(*tasks)
                    tasks = []
            return {"Result": "Payments processed."}


payment_handler = PaymentHandler()
