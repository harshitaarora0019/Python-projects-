balance = 0

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("₹", amount, "deposited.")
    else:
        print("Enter a valid amount!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Enter a valid amount!")
    else:
        balance -= amount
        print("₹", amount, "withdrawn.")

def check_balance():
    print("Your current balance is: ₹", balance)

while True:
    print("\n--- Welcome to My Bank App ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        check_balance()
    elif choice == '4':
        print("Thanks for using My Bank App!")
        break
    else:
        print("Invalid choice. Please try again.")
