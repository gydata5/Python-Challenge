# -*- coding: UTF-8 -*-
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
INPUT_PATH = os.path.join("Resources", "budget_data.csv")  # Input file path
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
month_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Open and read the csv
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_PATH) as csv_file:
    reader = csv.reader(csv_file)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    
    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
     # Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        month_list.append(row[0])

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]


# Calculate the average net change across the months
    if len(net_change_list) > 0:
         average_change = sum(net_change_list) / len(net_change_list)
    else:
         average_change = 0 # Handle case with no changes

# Generate the output summary
output = ( 
f"Financial Analysis\n"
f"-------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: ${average_change: .2f}\n" 
f"Greatest Profit Increase: {greatest_increase[0]} (${greatest_increase[1]})\n" 
f"Greatest Profit Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n" 
)

# Print the output
print(output)

# Write the results to a text file
with open(OUTPUT_PATH, "w") as txt_file:
    txt_file.write(output)

# Example analysis results
analysis_results = (
f"Summary of Analysis:\n"
f"-------\n"
f"- Total Months: 86\n"
f"- Average Change: -8311.11"
)
# Step 2: Print to the terminal
print(analysis_results)

# Step 3: Export to a text file
with open('analysis_results.txt', 'w') as file:
    file.write(analysis_results)