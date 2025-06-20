items = []
total = 0

while True:
    print("\n--- Billing Menu ---")
    print("1. Add item")
    print("2. View bill")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter quantity: "))
        cost = price * quantity
        items.append((name, price, quantity, cost))
        total += cost
        print(f"{quantity} x {name} added. Total: ₹{cost}")

    elif choice == '2':
        print("\n--- Your Bill ---")
        print("{:<10} {:<10} {:<10} {:<10}".format("Item", "Price", "Qty", "Total"))
        for item in items:
            print("{:<10} {:<10} {:<10} {:<10}".format(item[0], item[1], item[2], item[3]))
        print("Grand Total: ₹", total)

    elif choice == '3':
        print("Thank you for shopping! Final total: ₹", total)
        break

    else:
        print("Invalid option. Try again.")
