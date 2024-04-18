import csv

# Path to the CSV file
file_path = 'Resources/budget_data.csv'

# Initialize variables to store data
total_months = 0
total_profit_loss = 0
previous_profit_loss = None
monthly_change = []
greatest_increase = ["", 0]  # Date and amount
greatest_decrease = ["", 0]  # Date and amount

# Open the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)  # Skip the header row

    # Process each row in the CSV file
    for row in csv_reader:
        date, profit_loss = row
        profit_loss = int(profit_loss)

        # Count total months and sum total profit/loss
        total_months += 1
        total_profit_loss += profit_loss

        # Calculate monthly change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            monthly_change.append(change)

            # Check for greatest increase and decrease in profits
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        # Update previous profit/loss for next iteration
        previous_profit_loss = profit_loss

# Calculate average change in profit/loss
average_change = sum(monthly_change) / len(monthly_change) if monthly_change else 0

# Print the analysis to the terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Output path for the results text file
output_path = 'analysis/financial_analysis.txt'
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

