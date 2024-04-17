# Import the operating system and csv modules
import os
import csv

print("Financial Analysis")
print("----------------------------")

# map the resource file
budget_data = os.path.join("Resources", "budget_data.csv")

# read the CSV file and store in csvreader
with open(budget_data) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	# skip the column headers
	csv_header = next(csvreader)

	#define variables
	total_months = 0
	total_profit_loss = 0
	prev_month_profit_loss = 0.1
	profit_change = 0
	
	budget_data = []
	# loop through rows of data
	for x in csvreader:
		# calculate total "Profit/Losses" over the entire period
		month_profit_loss = int(x[1])
		total_profit_loss += month_profit_loss
		# calculate changes in "Profit/Losses" for each month
		if prev_month_profit_loss != 0.1:
			profit_change = month_profit_loss - prev_month_profit_loss
		# create dictionary to analyze greatest increase and decrease
		date = x[0]
		profit_loss = float(x[1])
		budget_data.append({
			"Date": date,
			"Profit Losses": profit_loss,
			"Profit Change": profit_change
			})
		prev_month_profit_loss = month_profit_loss

	# calculate and display total number of months included in the dataset
	total_months = (len(budget_data))
	print(f"Total Months: ", total_months)
	
	# display net total "Profit/Losses" over the entire period
	print(f"Total: $", total_profit_loss)
	
	# calculate and display changes in "Profit/Losses" over the entire period, and then the average of those changes
	average_change = round(((sum([month["Profit Change"] for month in budget_data]))) / (total_months -1), 2)
	print(f"Average Change: $", average_change)
	
	# calculate and display greatest increase in profits
	max_change = round(max([month["Profit Change"] for month in budget_data]))
	for month in budget_data:
		if month["Profit Change"] == max_change:
			print(f"Greatest Increase in Profits: ", month["Date"],  " ($", max_change, ")")
	
	# calculate and display greatest decrease in profits
	min_change = round(min([month["Profit Change"] for month in budget_data]))
	for month in budget_data:
		if month["Profit Change"] == min_change:
			print(f"Greatest Decrease in Profits: ", month["Date"], " ($", min_change, ")")
	