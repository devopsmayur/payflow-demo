"""Refund processing for PayFlow demo."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from payments.charge import ChargeResult


class RefundError(Exception):
    """Raised when a refund cannot be processed."""


@dataclass
class RefundResult:
    refund_id: str
    charge_id: str
    amount: Decimal
    status: str


def refund(original_charge: ChargeResult, amount: Optional[Decimal] = None) -> RefundResult:
    """Refund all or part of a previously completed charge.

    Args:
        original_charge: The ChargeResult being refunded.
        amount: Amount to refund. Defaults to the full charge amount.

    Returns:
        RefundResult describing the processed refund.

    Raises:
        RefundError: If the refund amount exceeds the original charge.
    """
    refund_amount = amount if amount is not None else original_charge.amount

    if refund_amount > original_charge.amount:
        raise RefundError(
            f"Refund amount {refund_amount} exceeds original charge {original_charge.amount}"
        )

    refund_id = f"re_{original_charge.charge_id}"

    return RefundResult(
        refund_id=refund_id,
        charge_id=original_charge.charge_id,
        amount=refund_amount,
        status="succeeded",
    )
