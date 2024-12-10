from abc import ABC, abstractmethod

from app.schemas.debt import CustomerDebt


class PaymentEngine(ABC):
    @abstractmethod
    async def process_payment(self, customer_debt: CustomerDebt):
        pass
