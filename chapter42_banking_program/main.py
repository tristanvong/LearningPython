def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount < 0:
        print("You can not deposit a negative amount.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program 2000")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        user_choice = int(input("Choose an option (1, 2, 3 or 4): "))

        match user_choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("Unknown input, closing program")
                is_running = False

if __name__ == '__main__':
    main()