"""Expense Splitter - Calculate how much each person should pay for a bill."""

def expense_split(total_bills, num_person, tip) -> tuple[float, float, float]:
    """Calculate expense split including tip.

    Args:
        total_bills: Total bill amount
        num_person: Number of people splitting the bill
        tip: Tip percentage

    Returns:
        Tuple of (per_person_amount, total_with_tip, tip_amount)
    """
    tip_dec = tip / 100
    tip_amount = total_bills * tip_dec
    final_amount = total_bills + tip_amount
    each_amount = final_amount / num_person

    return each_amount, final_amount, tip_amount


if __name__ == "__main__":
    # input
    total_bill = float(input("Enter Total Bill amount:"))
    num_person = int(input("Total person to split:"))
    tip = float(input("Tip percentage:"))
    result, total, tip = expense_split(total_bill, num_person, tip)

    print("=" * 50)
    # display output
    print(f"Bill: {total_bill:.2f}")
    print(f"Tip: {tip:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Each person Pays: {result:.2f}")
