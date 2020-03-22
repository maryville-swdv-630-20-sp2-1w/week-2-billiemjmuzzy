class CheckingAccount:
    """
    Implements checking account functionality

    Main methods:
        get_account:    returns account number
        get_balance:    returns current balance
        get_full_name:  returns full name
        deposit:        adds funds to account
        withdrawl:      remove funds from account
    """

    def __init__(self, account, balance, name, address):
        """
        Initializer to calculate bank balance
        @params
            account: account number
            balance: total balance
            name: full name 
            address: full address
        """
        self.__account_number = account
        self.__balance = balance
        self.__full_name = name
        self.__address = address

    def get_account(self):
        """
        Method to return account number
        """
        return self.__account_number

    def get_balance(self):
        """
        Method to return balance
        """
        return "{:.2f}".format(self.__balance)

    def get_full_name(self):
        """
        Method to return name
        """
        return self.__full_name

    def get_address(self):
        """
        Method to return address
        """
        return self.__address

    def deposit(self, amount):
        """
        Method to debit account
        """
        self.__balance += amount
        return self.__balance

    def withdrawl(self, amount):
        """
        Method to credit account
        """
        self.__balance -= amount
        return self.__balance
