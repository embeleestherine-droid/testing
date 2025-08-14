class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def authenticate(self):
        entered_pin = input("Enter your ATM PIN: ")
        return entered_pin == self.pin

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            self.check_balance()
        else:
            print("Insufficient balance or invalid amount.")

    def run(self):
        if not self.authenticate():
            print("Incorrect PIN. Access denied.")
            return

        while True:
            print("\n==== MENU ====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: $"))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == "4":
                print("Thank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


# ===== Run the ATM Program =====
if __name__ == "__main__":
    my_atm = ATM(pin="1234", balance=5000)
    my_atm.run()

#nice
#nice