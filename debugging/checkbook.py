class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance checking.
    """

    def __init__(self):
        """
        Initialize the checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add the specified amount to the balance.

        Parameters:
        amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtract the specified amount from the balance if funds are sufficient.

        Parameters:
        amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to interact with the user for managing the checkbook.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive.")
                    continue
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive.")
                    continue
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
