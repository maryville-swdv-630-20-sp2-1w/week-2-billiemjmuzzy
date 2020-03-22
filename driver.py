import json
import sys
from CheckingAccount import *

# Driver Code


def main():
    # read file
    with open('data.json') as file:
        data = json.load(file)

        try:
            # data.json only has accounts 11111 or 22222
            acct = input("Please input your account number: ")
            balance = data[acct]["balance"]
            name = (data[acct]["name"]["first_name"],
                    data[acct]["name"]["last_name"])
            address = (data[acct]["address"]["street"], data[acct]["address"]["city"],
                       data[acct]["address"]["state"], data[acct]["address"]["zip"])
        except:
            print("Account does not exist, please start your transaction over")
            sys.exit(1)

    my_account = CheckingAccount(
        acct, balance, name, address)

    print(f"Welcome, {my_account.get_full_name()[0]}, to the Bank of Billie ")

    def print_balance():
        # function to print balance
        print(f"Your current balance is ${my_account.get_balance()}.")

    def prompt():
        # function to prompt user
        choice = input(
            f'''
        Please select:
        [b] for current balance
        [w] for withdrawl
        [d] for deposit
        [i] for account information
        any other key to quit:

            ''')
        if choice.lower() == 'b' or choice.lower() == 'w' or choice.lower() == 'd' or choice.lower() == 'i':
            while choice:
                if choice.lower() == 'b':
                    print_balance()
                elif choice.lower() == 'w':
                    amount = float(
                        input("Please input the amount you would like to withdraw: "))
                    my_account.withdrawl(amount)
                    print_balance()
                elif choice.lower() == 'd':
                    amount = float(
                        input("Please input the amount you would like to deposit: "))
                    my_account.deposit(amount)
                    print_balance()
                elif choice.lower() == 'i':
                    print(
                        f"""
                    Name:           {my_account.get_full_name()[0]} {my_account.get_full_name()[1]}
                    Account Number: {my_account.get_account()}
                    Address:        {my_account.get_address()[0]}
                                    {my_account.get_address()[1]}, {my_account.get_address()[2]} {my_account.get_address()[3]}
                    Balance:        ${my_account.get_balance()}
                        """
                    )
                else:
                    print("Thank you for banking with Bank of Billie!")
                    sys.exit(1)

                choice = input(
                    f'''
        Please select:
        [b] for current balance
        [w] for withdrawl
        [d] for deposit
        [i] for account information
        any other key to quit:

                ''')
        else:
            print("Thank you for banking with Bank of Billie!")

    prompt()


main()
