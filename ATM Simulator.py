balance = 5000
pin = "1234"

def check_balance():
    print("Current Balance =", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Please collect your cash")
    else:
        print("Insufficient Balance")

entered_pin = input("Enter ATM PIN: ")

if entered_pin == pin:

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")
