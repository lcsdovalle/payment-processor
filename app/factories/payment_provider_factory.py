# app/services/payment/payment_factory.py
from app.helpers.constants import (
    PAG_BANK_PROVIDER_NAME,
    PAYPAL_PROVIDER_NAME,
    STRIPE_PROVIDER_NAME,
)
from app.interfaces.payment_engine import PaymentEngine
from app.schemas.payment import PaymentProviderName
from app.services.payment.pagbank_service import PagBankService
from app.services.payment.paypal_service import PayPalService
from app.services.payment.stripe_service import StripeService


class PaymentFactory:
    @staticmethod
    def get_payment_service(provider: PaymentProviderName) -> PaymentEngine:
        """
        Factory method to return the appropriate payment service.

        Args:
            provider (str): The payment provider name (e.g., "pagbank", "paypal", "stripe").

        Returns:
            PaymentEngine: An instance of the corresponding payment service.
        """
        if provider.value == PAG_BANK_PROVIDER_NAME:
            return PagBankService()
        elif provider.value == PAYPAL_PROVIDER_NAME:
            return PayPalService()
        elif provider.value == STRIPE_PROVIDER_NAME:
            return StripeService()
        else:
            raise ValueError(f"Unsupported payment provider: {provider}")
