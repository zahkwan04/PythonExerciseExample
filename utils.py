"""Shared utilities for exercise programs."""


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
