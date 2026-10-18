class BankAccount:
                                                                      # Constructor method that initializes a new BankAccount object with account_number and balance
    def __init__(self, account_number: int, balance: float):
        self.__account_number = 0
        self.__balance = 0.0

        self.set_account_number(account_number)
        self.set_balance(balance)

                                                                      # Getter methods using @property decorator
    @property                                                         # Getter method using @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def balance(self) -> float:                                       # Getter method using @propert
        return self.__balance

                                                                      # Public Setter methods
    def set_account_number(self, account_number: int):                # Setter method to update and set the private account_number attribute
        """Setter for account_number."""
        self.__account_number = account_number

    def set_balance(self, balance: float):                            # Setter method to update the private balance attribute with negative validation check
        """Setter for balance with negative check validation."""
        if balance < 0:
            print("The balance must be not be a negative number.")
        else:
            self.__balance = float(balance)


                                                                       # sample/test run vv
if __name__ == "__main__":
    a1 = BankAccount(int(input("Account Number: ")), float(input("Balance: ")))          # Create an object of class BankAccount taking values directly via input functions

    print("\nAccount 1")
    print(f"Account Number: {a1.account_number}")
    print(f"Balance: {a1.balance:.2f}\n")

    while True:                                                                              # Update balance using an input function
        updated_balance_input = float(input("Update balance to: "))
        if updated_balance_input < 0:                                                    # Check if the input is negative
            print("The balance must be not be a negative number.")
        else:
            a1.set_balance(updated_balance_input)                                        # If valid, use the setter to apply the balance and break out of the loop
            break

    print(f"Account Number: {a1.account_number}")
    print(f"Balance: {a1.balance:.2f}")