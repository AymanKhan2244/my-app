# pyrefly: ignore [missing-import]
import pytest

from app import calculate_tax


def test_calculate_tax_standard():
    assert calculate_tax(100.0) == 5.0


def test_calculate_tax_negative():
    with pytest.raises(ValueError):
        calculate_tax(-10.0)
