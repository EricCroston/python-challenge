# Import the operating system and csv modules
import os
import csv

print("Financial Analysis")
print("----------------------------")

# map the resource file
budget_data = os.path.join("Resources", "budget_data.csv")

# read the CSV file and store in csvreader
with open(budget_data, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	# skip the column headers
	csv_header = next(csvreader)

	#define the variables
	total_months = 0
	total_profit_loss = 0
	months = []

	# loop through rows of data
	for x in csvreader:
		# calculate total number of months included in the dataset
		total_months += 1
		# calculate total "Profit/Losses" over the entire period
		month_profit_loss = int(x[1])
		total_profit_loss = total_profit_loss + month_profit_loss
		# calculate changes in "Profit/Losses" over the entire period
		# create dictionary to analyze greatest increase and decrease
		date = x[0]
		profit_loss = float(x[1])
		months.append(
			{"Date": date,
			"Profit_Losses": profit_loss}
			)
	
	# display total number of months included in the dataset
	print("Total Months: " + str(total_months))
	
	# display net total "Profit/Losses" over the entire period
	print("Total: $" + str(total_profit_loss))
	


	# calculate and display changes in "Profit/Losses" over the entire period, and then the average of those changes

	
	# calculate and display greatest increase in profits
	max_profit = round(max([month["Profit_Losses"] for month in months]))
	for month in months:
		if month["Profit_Losses"] == max_profit:
			print("Greatest Increase in Profits: " + str(month["Date"]) + " ($" + str(max_profit) +")")
	
	# calculate and display greatest decrease in profits
	min_profit = round(min([month["Profit_Losses"] for month in months]))
	for month in months:
		if month["Profit_Losses"] == min_profit:
			print("Greatest Decrease in Profits: " + str(month["Date"]) + " ($" + str(min_profit) +")")
	