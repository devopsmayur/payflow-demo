
"""Payment charge processing for PayFlow demo."""

from dataclasses import dataclass
from decimal import Decimal


class ChargeError(Exception):
    """Raised when a charge cannot be processed."""


@dataclass
class ChargeResult:
    charge_id: str
    amount: Decimal
    currency: str
    status: str


MAX_CHARGE_AMOUNT = Decimal("10000.00")


def charge(customer_id: str, amount: Decimal, currency: str = "USD") -> ChargeResult:
    """Charge a customer's default payment method.

    Args:
        customer_id: Internal customer identifier.
        amount: Amount to charge, in the given currency.
        currency: ISO 4217 currency code.

    Returns:
        ChargeResult describing the processed charge.

    Raises:
        ChargeError: If the amount is invalid, exceeds the maximum allowed,
            or the charge is declined.
    """
    if amount <= 0:
        raise ChargeError(f"Charge amount must be positive, got {amount}")
    if amount > MAX_CHARGE_AMOUNT:
        raise ChargeError(
            f"Charge amount {amount} exceeds maximum allowed {MAX_CHARGE_AMOUNT}"
        )

    # In production this calls out to the payment gateway.
    charge_id = f"ch_{customer_id}_{int(amount * 100)}"

    return ChargeResult(
        charge_id=charge_id,
        amount=amount,
        currency=currency,
        status="succeeded",
    )
EOF