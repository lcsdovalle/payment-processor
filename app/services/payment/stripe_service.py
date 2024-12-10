from app.interfaces.payment_engine import PaymentEngine
from app.schemas.debt import CustomerDebt


class StripeService(PaymentEngine):
    async def process_payment(self, customer_debt: CustomerDebt) -> bool:
        print(
            f"Processing payment of R$ {customer_debt.amount} for customer {customer_debt.email} using Stripe."
        )
        return True
