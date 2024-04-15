# Import the operating system and csv modules
import os
import csv

print("Financial Analysis")
print("----------------------------")

# map the resource file
budget_data = os.path.join("Resources", "budget_data.csv")

# read the CSV file and store in csvreader
with open(budget_data, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	# skip the column headers
	csv_header = next(csvreader)
	#print(csv_header)

	#define the variables
	total_months = 0
	total_profit_loss = 0
		
	# loop through rows of data
	for x in csvreader:
		#print(x)
		# calculate total number of months included in the dataset
		total_months += 1
		# calculate total "Profit/Losses" over the entire period
		month_profit_loss = int(x[1])
		total_profit_loss = total_profit_loss + month_profit_loss
		
		if int(x[1]) > nextrow[1]:
		 	greatest_profit_row = x

	# display total number of months included in the dataset
	print("Total Months: " + str(total_months))
	# display total "Profit/Losses" over the entire period
	print("Total: $" + str(total_profit_loss))
	# display greatest increase in profits (date and amount) over the entire period
	print("Greatest Increase in Profits: " + x[0] + " ($" + x[1] +")")


# The greatest increase in profits (date and amount) over the entire period
	
# The greatest decrease in profits (date and amount) over the entire period