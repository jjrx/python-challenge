# dependencies
import pandas as pd
import os

# import budget_data.csv into a dataframe
file = "Resources/budget_data.csv"
budget_df = pd.read_csv(file)

# calculate the total net profits/losses
sum_revenue = budget_df["Revenue"].sum()

# calculate the number of unique months
total_months = len(budget_df["Date"].unique())

# find the largest revenue increase
greatest_increase = budget_df["Revenue"].max()
# iterate through the data frame to find the month associated with the largest revenue increase
for index, row in budget_df.iterrows():
    if row["Revenue"] == greatest_increase:
        greatest_increase_month = row["Date"]

# find the largest revenue decrease
greatest_decrease = budget_df["Revenue"].min()
# iterate through the data frame to find the month associated with the largest revenue decrease
for index, row in budget_df.iterrows():
    if row["Revenue"] == greatest_decrease:
        greatest_decrease_month = row["Date"]

monthly_changes_list = []
initial = 0
final = 0
# iterate through the dataframe and append the difference between consecutive revenues
# and append this value to monthly_changes_list array
for index, row in budget_df.iterrows():
    if index == 0:
        initial = row["Revenue"]
    else:
        final = row["Revenue"]
        monthly_change = (final - initial)
        monthly_changes_list.append(monthly_change)
        initial = final 

# find the sum of monthly changes in the array
change_sum = 0
for change in monthly_changes_list:
    change_sum += change
# calculate the average monthly change by dividing the sum of the list by the number of items in the list
average_change = change_sum/len(monthly_changes_list)

# display results in .txt file
output_file = os.path.join("Resources", "PyBank_Results.txt")
with open(output_file, "w") as datafile:
    datafile.writelines([
        "Financial Analysis\n",
        "----------------------------\n",
        f"Total Months: {total_months}\n",
        f"Total: ${sum_revenue}\n",
        f"Average Change: ${average_change}\n",
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n",
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    ])

# print out results in terminal
with open(output_file, "r") as f:
    results = f.read()
    print(results)

