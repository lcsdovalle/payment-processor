from enum import Enum

from app.helpers.constants import (
    PAG_BANK_PROVIDER_NAME,
    PAYPAL_PROVIDER_NAME,
    STRIPE_PROVIDER_NAME,
)


class PaymentProviderName(str, Enum):
    PAYPAL = PAYPAL_PROVIDER_NAME
    PAGBANK = PAG_BANK_PROVIDER_NAME
    STRIPE = STRIPE_PROVIDER_NAME
