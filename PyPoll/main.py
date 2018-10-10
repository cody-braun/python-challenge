import os
import csv

num_votes = 0
results = {}

with open('election_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader, None)

    for row in csvreader:
        if not row[2] in results:
            results[row[2]] = 1
        else:
            results[row[2]] += 1

print("Election Results\n-------------------------")
print(f"Total Votes: {sum(results.values())}")
print("-------------------------")

results_sorted = [(val,key) for key,val in results.items()]

for val,key in results_sorted:
    print(f"{key}: {val/sum(results.values()):.2%} ({val})")

print("-------------------------")
print(f"Winner: {results_sorted[0][1]}")
print("-------------------------")

with open('election_summary.txt', mode='w') as txtfile:
    
    text_to_write = ["Election Results\n",
    "-------------------------\n",
    f"Total Votes: {sum(results.values())}\n",
    "-------------------------\n"]

    txtfile.writelines(text_to_write)

    for val,key in results_sorted:
        txtfile.writelines(f"{key}: {val/sum(results.values()):.2%} ({val})\n")

    text_to_write = ["-------------------------\n",
    f"Winner: {results_sorted[0][1]}\n",
    "-------------------------"]

    txtfile.writelines(text_to_write)