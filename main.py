import os
import csv

file_location = os.path.join("C:", "Users", "under", "Python-challenge", "PyBank", "Resources", "budget_data.csv")

# Initialize variables
total_number_months = 0
net_total_Profit_losses = 0
previous_profit_loss = 0
total_change = 0
max_increase = ["", 0]
max_decrease = ["", 0]

# Read the CSV file and skip the header
with open(file_location, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header

    # Loop through each row in the CSV file
    for row in csvreader:
        # Count total months
        total_number_months += 1
        # Calculate net total profit/loss and convert to integer
        net_total_Profit_losses += int(row[1])
        # Calculate change in profit/loss
        if previous_profit_loss != 0:
            change = int(row[1]) - previous_profit_loss
            total_change += change
            # Determine greatest increase and decrease
            if change > max_increase[1]:
                max_increase = [row[0], change]
            if change < max_decrease[1]:
                max_decrease = [row[0], change]
        previous_profit_loss = int(row[1])  # Update previous profit/loss for next iteration

# Calculate average change (divide by total_number_months - 1)
average_change = total_change / (total_number_months - 1)

# Print analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_months}")
print(f"Total: ${net_total_Profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Max Increase in Profits: {max_increase[0]} (${max_increase[1]})")
print(f"Max Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")
