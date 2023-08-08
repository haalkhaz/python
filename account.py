class Account:
    def __init__(self, name: str):
        """
        Initialize a new Account instance.

        :param name: The name associated with the account.
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Deposit funds into the account.

        :param amount: The amount to be deposited.
        :return: True if the deposit is successful, False otherwise.
        """
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw funds from the account.

        :param amount: The amount to be withdrawn.
        :return: True if the withdrawal is successful, False otherwise.
        """
        if amount <= 0 or amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Retrieves the current account balance.

        :return: The current account balance.
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        Retrieves the account name.

        :return: The account name.
        """
        return self.account_name
