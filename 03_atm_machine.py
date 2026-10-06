"""ATM Machine Simulation - Simple banking operations."""


def get_positive_value(prompt: str) -> float | None:
    """Get positive numeric input from user.

    Args:
        prompt: Input prompt message

    Returns:
        Positive float value or None if invalid
    """
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


def check_balance(balance: float) -> float:
    """Display current balance.

    Args:
        balance: Current account balance

    Returns:
        Current balance
    """
    print("="*40 + "Current Balance" + "="*40)
    print(f"Your current balance is: ${balance:.2f}")

    return balance


def deposit_money(balance: float) -> float:
    """Deposit money into account.

    Args:
        balance: Current account balance

    Returns:
        Updated account balance
    """
    print("="*40 + "Deposit Money" + "="*40)
    deposit_amount = get_positive_value("Enter the amount to deposit: $")

    # implement guard clauses / negative case first
    if deposit_amount is None:
        return balance

    print(f"Depositing ${deposit_amount:.2f}")
    balance += deposit_amount
    print(f"Your balance is ${balance:.2f}")
    return balance


def withdraw_money(balance: float) -> float:
    """Withdraw money from account.

    Args:
        balance: Current account balance

    Returns:
        Updated account balance
    """
    print("="*40 + "Withdraw Money" + "="*40)
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


def exit_atm(balance: float) -> float:
    """Exit ATM application.

    Args:
        balance: Current account balance

    Returns:
        Current account balance
    """
    print("="*40 + "Exit ATM" + "="*40)
    print("Thank you for using this ATM services. Have a nice day!")
    return balance


def run_atm(balance: float) -> None:
    """Run ATM application main loop.

    Args:
        balance: Starting account balance
    """
    # Dictionary mapping key -> (Display Text, Function Reference)
    menu = {
        "1": ("Check balance", check_balance),
        "2": ("Deposit money", deposit_money),
        "3": ("Withdraw money", withdraw_money),
        "4": ("Exit", exit_atm),
    }

    while True:
        print("\n" + "="*55 + "Welcome to this ATM Machine Service")

        # Dynamically render all menu choices
        for option_num, (label, _) in menu.items():
            print(f"{option_num}. {label}")

        choice = input("Choose option number: ").strip()

        # Guard clause for invalid selection
        if choice not in menu:
            print(f"Invalid input. Enter an option between 1 and {len(menu)} only!")
            continue

        label, action = menu[choice]
        balance = action(balance)

        if choice == "4":
            break


if __name__ == "__main__":
    run_atm(1000.0)
