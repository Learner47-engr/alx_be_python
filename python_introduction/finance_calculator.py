income = int(input("Enter your monthly income"))
expenses = int(input("Enter your monthly total expenses"))

savings = income - expenses

Projected_Savings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly savings are $"+ str(savings))
# print("Projected savings after one year, with interest, is: $",Projected_Savings)
print("Projected savings after one year, with interest, is: $" + str(Projected_Savings))

# print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")