# Demo PR: add a maximum charge limit

This is the smallest change that's unambiguously "user-facing behavior" —
important for making the changelog action fire reliably every time (see
note below).

In `payments/charge.py`, replace:

```python
def charge(customer_id: str, amount: Decimal, currency: str = "USD") -> ChargeResult:
    """Charge a customer's default payment method.

    Args:
        customer_id: Internal customer identifier.
        amount: Amount to charge, in the given currency.
        currency: ISO 4217 currency code.

    Returns:
        ChargeResult describing the processed charge.

    Raises:
        ChargeError: If the amount is invalid or the charge is declined.
    """
    if amount <= 0:
        raise ChargeError(f"Charge amount must be positive, got {amount}")
```

with:

```python
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
```

This is a real behavior change (large charges now get rejected), touches
`payments/charge.py` directly, and has an obvious PR description you can
write in one line: "Add a maximum single-charge limit to prevent
unintentionally large charges."
