import os
import csv

date, revenue = ([] for i in range(2))

csv1_path = os.path.join("data", "budget_data_1.csv")
csv2_path = os.path.join("data", "budget_data_2.csv")

with open(csv1_path, mode='r', newline='') as budget_data_1:
    reader_1 = csv.reader(budget_data_1, delimiter=',')

    next(reader_1)

    for row in reader_1:
        date.append(row[0])
        revenue.append(row[1])


with open(csv2_path, mode='r', newline='') as budget_data_2:
    reader_2 = csv.reader(budget_data_2, delimiter=',')

    next(reader_2)

    for row in reader_2:
        date.append(row[0])
        revenue.append(row[1])


# *-----------------*
# |  Summary Table  |
# *-----------------*

# print summary header
print("\nFinancial Analysis", "\n" + "-" * 50)

# sum of months
total_months = len(date)
print("Total Months:", total_months)


# sum of revenue
revenue_sum = 0
for i in revenue:
    revenue_sum += int(i)

print("Total Revenue: $" + str(revenue_sum))


# average revenue change
avg_revenue_change = revenue_sum / total_months
print("Average Revenue Change: $" + str(round(avg_revenue_change)))


# greatest increase in revenue

# FIRST ATTEMPT: ERROR - list index out of range
# for i in range(len(revenue) + 2):
#     if int(revenue[i]) + int(revenue[i + 1]) > int(revenue[i + 1]) + int(revenue[i + 2]):
#         high_revenue = int(revenue[i]) + int(revenue[i + 1])

print("Greatest Increase in Revenue:")


# greatest decrease in revenue
print("Greatest Decrease in Revenue:")
low_revenue = 0


# white space after table
print("\n\n")
