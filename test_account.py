import pytest
from account import Account

class TestAccount:
    def setup_method(self):
        self.a1 = Account("Alice")

    def test_init(self):
        account = Account("Bob")
        assert account.get_name() == "Bob"
        assert account.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == pytest.approx(100)

    def test_deposit_zero_amount(self):
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == pytest.approx(0)

    def test_deposit_negative_amount(self):
        assert self.a1.deposit(-50) is False
        assert self.a1.get_balance() == pytest.approx(0)

    def test_withdraw(self):
        self.a1.deposit(200)
        assert self.a1.withdraw(150) is True
        assert self.a1.get_balance() == pytest.approx(50)

    def test_withdraw_zero_amount(self):
        self.a1.deposit(75)
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == pytest.approx(75)

    def test_withdraw_insufficient_balance(self):
        self.a1.deposit(60)
        assert self.a1.withdraw(100) is False
        assert self.a1.get_balance() == pytest.approx(60)

    def test_withdraw_negative_amount(self):
        self.a1.deposit(50)
        assert self.a1.withdraw(-25) is False
        assert self.a1.get_balance() == pytest.approx(50)

if __name__ == "__main__":
    pytest.main()


