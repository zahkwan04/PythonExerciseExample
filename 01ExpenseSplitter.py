# 1. Expense Splitter

# You and your friends go out for dinner.

# Given:

# Total bill: €127.50
# Number of people: 4
# Tip: 10%

# Write a program that calculates how much each person should pay.

# Example output:

# Bill: €127.50
# Tip: €12.75
# Total: €140.25
# Each person pays: €35.06

def expenseSplit(total_bill, num_person, tip ) -> float:
    
    tip_dec = tip/100
    tip_amount = total_bill * tip_dec
    final_amount = total_bill + tip_amount
    each_amount = final_amount / num_person

    return each_amount, final_amount, tip_amount
    

#input
total_bill = float(input("Enter Total Bill amount:") )   
num_person = int(input("Total person to split:")   )
tip = float(input("Tip percentage:")   )
result, total, tip = expenseSplit(total_bill, num_person, tip)

print("==================================================\n")
#display output
print(f"Bill: {total_bill:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print(f"Each person Pays: {result:.2f}")