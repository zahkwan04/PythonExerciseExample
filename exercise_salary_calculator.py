"""Salary Calculator - Calculate net salary after deductions."""


def calculate_net(gross_salary, tax_pct, social_pct) -> tuple[float, float, float]:
    """Calculate net salary after tax and social contributions.

    Args:
        gross_salary: Gross salary
        tax_pct: Tax percentage
        social_pct: Social contribution percentage

    Returns:
        Tuple of (tax_deduction, social_deduction, net_salary)
    """
    tax_deduction = tax_pct / 100 * gross_salary
    social_deduction = social_pct / 100 * gross_salary
    net_salary_result = gross_salary - tax_deduction - social_deduction

    return tax_deduction, social_deduction, net_salary_result


def ask_input() -> tuple[float, float, float]:
    """Get salary and deduction percentages from user.

    Returns:
        Tuple of (gross_salary, tax_percent, social_contribution)
    """
    gross_salary_input = float(input("Enter your gross salary: $"))
    tax_percent_input = float(input("Enter Tax amount %: "))
    social_contribution_input = float(input("Enter Social Contribution %: "))

    return gross_salary_input, tax_percent_input, social_contribution_input


def display_output(gross_amt, tax_amt, social_amt, net_amt):
    """Display salary breakdown.

    Args:
        gross_amt: Gross salary
        tax_amt: Tax amount
        social_amt: Social contribution amount
        net_amt: Net salary
    """
    print("=" * 54 + "CALCULATED NET SALARY" + "=" * 54)
    print(f"Gross salary: ${gross_amt:.2f}")
    print(f"Tax: ${tax_amt:.2f}")
    print(f"Social Contribution: ${social_amt:.2f}")
    print(f"Net Salary: ${net_amt:.2f}")


if __name__ == "__main__":
    # Main
    gross_sal, tax_pct_val, social_pct_val = ask_input()
    tax_deduct, social_deduct, net_salary = calculate_net(gross_sal, tax_pct_val, social_pct_val)
    display_output(gross_sal, tax_deduct, social_deduct, net_salary)
