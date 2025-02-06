# Restaurant Bill Calculator

# Get the food charge from the user
food_charge = float(input("Enter the charge for the food: $"))

# Define tax and tip percentages
tip_rate = 0.18  # 18% tip
tax_rate = 0.07  # 7% sales tax

# Calculate tip and tax amounts
tip_amount = food_charge * tip_rate
tax_amount = food_charge * tax_rate

# Calculate total cost
total_cost = food_charge + tip_amount + tax_amount

# Display results
print("\n---- Receipt ----")
print(f"Food Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip_amount:.2f}")
print(f"Sales Tax (7%): ${tax_amount:.2f}")
print(f"Total Amount: ${total_cost:.2f}")
