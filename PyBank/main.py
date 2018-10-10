import os
import csv

num_months = 0
total_profit = 0
total_profit_change = 0
last_profit = 0
greatest_inc_amount = 0
greatest_inc_month = ""
greatest_dec_amount = 0
greatest_dec_month = ""

with open('budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        num_months += 1
        total_profit += float(row[1])
        if last_profit != 0:
            profit_change = (float(row[1]) - last_profit)
            total_profit_change += profit_change
            if profit_change > greatest_inc_amount:
                greatest_inc_amount = profit_change
                greatest_inc_month = row[0]
            if profit_change < greatest_dec_amount:
                greatest_dec_amount = profit_change
                greatest_dec_month = row[0]
        last_profit = float(row[1])

print("Financial Analysis\n-------------------------")
print(f"Total Month: {num_months}")
print(f"Total: ${int(total_profit)}")
print(f"Average Change: ${total_profit_change/num_months:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${int(greatest_inc_amount)})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${int(greatest_dec_amount)})")

with open('budget_summary.txt', mode='w') as txtfile:
    
    text_to_write = ["Financial Analysis\n",
    "-------------------------\n",
    f"Total Month: {num_months}\n",
    f"Total: ${int(total_profit)}\n",
    f"Average Change: ${total_profit_change/num_months:.2f}\n",
    f"Greatest Increase in Profits: {greatest_inc_month} (${int(greatest_inc_amount)})\n",
    f"Greatest Decrease in Profits: {greatest_dec_month} (${int(greatest_dec_amount)})\n"]

    txtfile.writelines(text_to_write)

    