"""Expense Tracker - Track expenses by category."""


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


def add_expenses(expenses: dict) -> dict:
    """Add expenses to tracker.

    Args:
        expenses: Dictionary of current expenses

    Returns:
        Updated expenses dictionary
    """
    category = {
        "1": "Food",
        "2": "Transport",
        "3": "Coffee",
        "4": "Shopping",
        "5": "Other",
        "6": "Done",
    }

    while True:
        print("="*35 + "Add expenses")
        print("Expense Category")

        # Dynamically render all menu choices
        for option_num, label in category.items():
            print(f"{option_num}. {label}")

        choice = input("Select number option:").strip()

        # Guard clause for invalid selection
        if choice not in category:
            print(f"Invalid input. Enter an option between 1 and {len(category)} only!")
            continue

        if choice == "6":
            return expenses

        expense_name = category[choice]

        if choice == "5":
            expense_name = custom_expenses()
            if not expense_name:
                continue

        amount = get_positive_value("Enter the expenses amount:$")
        if amount is None:
            continue

        # Add expenses
        expenses[expense_name] = expenses.get(expense_name, 0) + amount
        print(f"Added {expense_name}: ${amount:.2f}")


def display_expenses(expenses: dict) -> dict:
    """Display all tracked expenses.

    Args:
        expenses: Dictionary of expenses to display

    Returns:
        Expenses dictionary
    """
    print("="*40 + "Your Expenses List")
    if not expenses:
        print("No Expenses Recorded.")
        return expenses

    for expense_name, expense_total in expenses.items():
        print(f"{expense_name:<12} : ${expense_total:.2f}")

    total_expenses = sum(expenses.values())
    print(f"Total expenses: ${total_expenses:.2f}")

    highest = max(expenses, key=expenses.get)
    print(f"Highest Spending - {highest} : ${expenses[highest]:.2f}")

    return expenses


def exit_apps(expenses: dict) -> dict:
    """Exit application.

    Args:
        expenses: Final expenses dictionary

    Returns:
        Expenses dictionary
    """
    print("="*52 + "Exiting Expense Tracker App")
    print("Have a nice day!")
    return expenses


def custom_expenses() -> str | None:
    """Get custom expense category from user.

    Returns:
        Custom expense category name or None if cancelled
    """
    while True:
        expense_name = input("Enter what is this expense for (or enter 'q' to quit):")

        expense_name = expense_name.strip()

        if not expense_name:
            print("Name cannot be empty. Please try again")
            continue

        if expense_name.lower() == 'q':
            print("Operation cancelled.")
            return None

        return expense_name.capitalize()


def run_apps(expenses: dict) -> None:
    """Run expense tracker application main loop.

    Args:
        expenses: Starting expenses dictionary
    """
    # Dictionary mapping key -> (Display Text, Function Reference)
    menu = {
        "1": ("Add Expenses", add_expenses),
        "2": ("Display Expenses", display_expenses),
        "3": ("Exit", exit_apps),
    }

    while True:
        print("\n" + "="*55 + "Welcome to Expense Tracker Apps")

        # Dynamically render all menu choices
        for option_num, (label, _) in menu.items():
            print(f"{option_num}. {label}")

        choice = input("Choose option number: ").strip()

        # Guard clause for invalid selection
        if choice not in menu:
            print(f"Invalid input. Enter an option between 1 and {len(menu)} only!")
            continue

        _, action = menu[choice]
        expenses = action(expenses)

        if choice == "3":
            break


if __name__ == "__main__":
    run_apps({})
