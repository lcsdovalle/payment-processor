import pytest

from app.factories.payment_provider_factory import PaymentFactory
from app.schemas.payment import PaymentProviderName
from app.services.payment.pagbank_service import PagBankService
from app.services.payment.paypal_service import PayPalService
from app.services.payment.stripe_service import StripeService


def test_payment_factory():
    assert isinstance(
        PaymentFactory.get_payment_service(PaymentProviderName.PAGBANK), PagBankService
    )
    assert isinstance(
        PaymentFactory.get_payment_service(PaymentProviderName.PAYPAL), PayPalService
    )
    assert isinstance(
        PaymentFactory.get_payment_service(PaymentProviderName.STRIPE), StripeService
    )


def test_unsupported_payment_provider():
    with pytest.raises(AttributeError):
        PaymentFactory.get_payment_service("unknown_provider")
