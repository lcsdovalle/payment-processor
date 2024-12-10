import pytest
from app.helpers.providers import get_providers
from app.schemas.payment import PaymentProviderName

def test_get_providers():
    """
    Test helpers
    """
    valid_providers = {
        PaymentProviderName.PAGBANK,
        PaymentProviderName.PAYPAL,
        PaymentProviderName.STRIPE,
    }
    provider = get_providers()
    assert provider in valid_providers, f"Unexpected provider: {provider}"