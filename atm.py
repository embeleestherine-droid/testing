# Simple ATM Program in Python

# Initial account data
balance = 5000  # starting balance
pin = "1234"    # ATM PIN


# Authenticate user
print("==== Welcome to Python ATM ====")
entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    while True:
        print("\n==== MENU ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == "1":
            print(f"\nYour current balance is: ${balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: $"))
            if amount > 0:
                balance += amount
                print(f"${amount:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: $"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "4":
            print("Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect PIN. Access denied.")

#this code has a problem with showing the balance
#maybe we need to relook at it