from decimal import Decimal

import pytest

from payments.charge import charge, ChargeError


def test_charge_succeeds():
    result = charge("cust_123", Decimal("49.99"))
    assert result.status == "succeeded"
    assert result.amount == Decimal("49.99")


def test_charge_rejects_non_positive_amount():
    with pytest.raises(ChargeError):
        charge("cust_123", Decimal("0"))
