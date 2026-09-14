# Input:

# Gross salary: 3000
# Tax: 18%
# Social contribution: 9%

# Calculate:

# Tax amount
# Social contribution
# Net salary

# Then display something like:

# Gross salary: €3000
# Tax: €540
# Social contribution: €270
# Net salary: €2190


#user input -> calculate -> display

def calculateNet(gross , tax, social_cont) -> tuple[float,float,float]:
    tax_deduction = tax/100*gross
    social_deduction = social_cont/100*gross
    net_salary = gross - tax_deduction - social_deduction

    return tax_deduction, social_deduction, net_salary

def askInput() -> tuple[float,float,float]:
    grossSalary = float(input("Enter your gross salary: $"))
    taxPercent = float(input("Enter Tax amount %: "))
    socialContribution = float(input("Enter Social Contribution %: "))

    return grossSalary, taxPercent, socialContribution

def displayOutput(gross, tax, social, net):
    print("===============CALCULATED NET SALARY==================")
    print(f"Gross salary: ${gross:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Social Contribution: ${social:.2f}")
    print(f"Net Salary: ${net:.2f}")

#Main
gross, tax, social = askInput()
taxDeduct, socialDeduct, netSalary = calculateNet(gross, tax, social)
displayOutput(gross, taxDeduct, socialDeduct, netSalary)

