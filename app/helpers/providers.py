import random

from app.schemas.payment import PaymentProviderName


def get_providers() -> str:
    return random.choice(
        [
            PaymentProviderName.PAGBANK,
            PaymentProviderName.PAYPAL,
            PaymentProviderName.STRIPE,
        ]
    )
