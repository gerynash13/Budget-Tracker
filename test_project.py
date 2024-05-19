from decimal import Decimal
from project import deposit, expenses, balance

def main():
    test_deposit()
    test_expenses()
    test_balance()

# Test deposit function
def test_deposit():
    assert deposit("100€", "salary") == Decimal("100")
    assert deposit("100", "salary") == Decimal("200")
    assert deposit("invalid amount", "salary") == Decimal("200")
    assert deposit("49.50€", "salary") == Decimal("249.50")
    assert deposit("50.50", "salary") == Decimal("300")

def test_expenses():
    assert expenses("50€", "housing") == Decimal("250")
    assert expenses("50", "housing") == Decimal("200")
    assert expenses("49.50€", "housing") == Decimal("150.50")
    assert expenses("50.50", "housing") == Decimal("100")
    assert expenses("invalid amount", "housing") == Decimal("100")

def test_balance():
    assert balance("check balance") == Decimal("100")
    assert balance("view income") == Decimal("100")
    assert balance("view expenses") == Decimal("100")
