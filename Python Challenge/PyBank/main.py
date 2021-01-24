import csv
import os

input_file = "Resources/budget_data.csv"


print("  Financial Analysis  ")

print("------------------------")

total_profit = []
total_months = []
rev_change = []

with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for x in range(len(total_profit)-1):
        rev_change.append(total_profit[x + 1]-total_profit[x])
    
    print(f"Total Months :  {len(total_months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average change : {round(sum(rev_change) / len(rev_change), 2)}")

    greatest_increase = max(rev_change)

    greatest_decrease = min(rev_change)

    print("Greatest Increase in Profits: " + str(total_months[rev_change.index(max(rev_change)) + 1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(total_months[rev_change.index(min(rev_change)) + 1]) + " " + "$" + str(greatest_decrease))

output_file = "Resources/Financial_analysis.txt"

with open(output_file, "w") as file:
    file.write("   Financial Analysis  ")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Months : {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(rev_change) / len(rev_change), 2)}")
    file.write("\n")
    file.write("Greatest Increase in Profits: " + str(total_months[rev_change.index(max(rev_change)) + 1]) + " " + "$" + str(
        greatest_increase))
    file.write("\n")
    file.write("Greatest Decrease in Profits: " + str(total_months[rev_change.index(min(rev_change)) + 1]) + " " + "$" + str(
        greatest_decrease))
