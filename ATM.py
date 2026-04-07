# create  a project to start transaction on a ATM machine
correct_pin = "1234"
balance = 1000

pin = input("Enter your PIN: ")
#using pin to check if the user is authorized to access the account

if pin == correct_pin:
    print("Login successful.")
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

# Presenting the user with options to check balance, deposit, withdraw, or exit the ATM.
        choice = input("Enter choice: ")
        
        if choice == '1':
            print(f"Your balance is: ${balance}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposit successful. Your balance is: ${balance}")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. Your balance is: ${balance}")
            else:
                print("Insufficient funds.")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break   
        else: 
            print("Invalid choice. Please try again.")

        

