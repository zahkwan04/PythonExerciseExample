"""Salary Calculator - Calculate net salary after deductions."""


def calculate_net(gross, tax, social_cont) -> tuple[float, float, float]:
    """Calculate net salary after tax and social contributions.

    Args:
        gross: Gross salary
        tax: Tax percentage
        social_cont: Social contribution percentage

    Returns:
        Tuple of (tax_deduction, social_deduction, net_salary)
    """
    tax_deduction = tax / 100 * gross
    social_deduction = social_cont / 100 * gross
    net_salary = gross - tax_deduction - social_deduction

    return tax_deduction, social_deduction, net_salary


def ask_input() -> tuple[float, float, float]:
    """Get salary and deduction percentages from user.

    Returns:
        Tuple of (gross_salary, tax_percent, social_contribution)
    """
    gross_salary = float(input("Enter your gross salary: $"))
    tax_percent = float(input("Enter Tax amount %: "))
    social_contribution = float(input("Enter Social Contribution %: "))

    return gross_salary, tax_percent, social_contribution


def display_output(gross, tax, social, net):
    """Display salary breakdown.

    Args:
        gross: Gross salary
        tax: Tax amount
        social: Social contribution amount
        net: Net salary
    """
    print("=" * 54 + "CALCULATED NET SALARY" + "=" * 54)
    print(f"Gross salary: ${gross:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Social Contribution: ${social:.2f}")
    print(f"Net Salary: ${net:.2f}")


if __name__ == "__main__":
    # Main
    gross, tax, social = ask_input()
    tax_deduct, social_deduct, net_salary = calculate_net(gross, tax, social)
    display_output(gross, tax_deduct, social_deduct, net_salary)
