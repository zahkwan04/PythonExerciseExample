# Make a simple ATM program.
# Starting balance: €1000

# Allow the user to:

# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. Exit

# Rules:

# Cannot withdraw more than the balance.
# Cannot deposit negative amounts.
# After every transaction, show the balance.

# Example:

# ===== ATM =====
# 1. Check balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# Choose: 3
# Amount: 250

# Withdrawal successful.
# Remaining balance: €750

# This is a good exercise for functions + loops + if/else.

def get_positive_value(prompt:str)-> float | None:
    raw = input(prompt)
    try:
        amount = float(raw)
    except ValueError:
        print("Invalid input - please enter number only.")
        return None
    
    if amount <= 0:
        print("Amount must be greater than zero")
        return None
    
    return amount


def check_balance(balance) -> float:
    print("============Current Balance============")
    print(f"Your current balance is: ${balance:.2f}")  

    return balance


def deposit_money(balance) -> float:
    print("============Deposit Money============")
    deposit_amount = get_positive_value("Enter the amount to deposit: $")

    # implement guard clauses / negative case first
    if deposit_amount is None:
        return balance

    print(f"Depositing ${deposit_amount:.2f}")
    balance += deposit_amount
    print(f"Your balance is ${balance:.2f}")
    return balance



def withdraw_money(balance) -> float:
    print("============Withdraw Money============")
    withdraw_amount = get_positive_value("Enter the amount to withdraw: $")

    # implement guard clauses / negative case first
    if withdraw_amount is None:
        return balance
    
    if withdraw_amount > balance:
        print("\nInvalid amount to withdraw!")
        return balance
    
    print(f"Withdrawing ${withdraw_amount:.2f} from your account.")
    balance -= withdraw_amount
    print(f"Your balance is ${balance:.2f}")
    return balance


def exit_atm():
    print("===========Exit ATM============")
    print("Thank you for using this ATM services. Have an nice day!")


def run_atm(balance):
    while True:
        print("\n========Welcome to this ATM Machine Service===========")
        print("Please choose the number from options in the menu below")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")

        choice = input("Choose option number:").strip()
        if choice == "1":
            balance = check_balance(balance)
        elif choice == "2":
            balance = deposit_money(balance)
        elif choice == "3":
            balance = withdraw_money(balance)
        elif choice == "4":
            exit_atm()
            break
        else:
            print("Invalid input. Enter option between 1 - 4 only!")


if __name__ == "__main__":
    run_atm(1000.0)