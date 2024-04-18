# Import the operating system and csv modules
import os
import csv

# map the resource file
election_data = os.path.join("Resources", "election_data.csv")

# read the CSV file and store in csvreader
with open(election_data) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	# store and skip the column headers
	csv_header = next(csvreader)

	# convert data to dictionary of lists
	election_data = []
	candidates = []
	for x in csvreader:
		ballot_id = x[0]
		county = x[1]
		candidate = x[2]
		election_data.append({
			"Ballot ID": ballot_id,
			"County": county,
			"Candidate": candidate,
			})
		candidates.append(candidate)

	# find candidate names and calculate total number of votes each candidate won
	candidate_one = 'name'
	candidate_two = 'name'
	candidate_three = 'name'
	for x in candidates:
		if candidate_one == 'name':
			candidate_one = x
		elif candidate_one != x and candidate_two == 'name':
			candidate_two = x
		elif candidate_one != x and candidate_two != x and candidate_three == 'name':
			candidate_three = x
	candidate_one_votes = 0
	candidate_two_votes = 0
	candidate_three_votes = 0
	for x in candidates:
		if x == candidate_one:
			candidate_one_votes += 1
		elif x == candidate_two:
			candidate_two_votes += 1
		elif x == candidate_three:
			candidate_three_votes += 1
	
	# create output variables
	header = ("Election Results")
	seperator = ("-------------------------")

	# calculate and create output variables for total number of votes
	total_votes = (len(election_data))
	total_votes_output = ('Total Votes: ' + str(total_votes))

	# calculate and create output variables for percentage of votes each candidate won
	candidate_one_percentage = (candidate_one_votes / total_votes) * 100
	candidate_one_percentage = round(candidate_one_percentage, 3)
	candidate_two_percentage = (candidate_two_votes / total_votes) * 100
	candidate_two_percentage = round(candidate_two_percentage, 3)
	candidate_three_percentage = (candidate_three_votes / total_votes) * 100
	candidate_three_percentage = round(candidate_three_percentage, 3)

	# create output variables for candidate name, percentage votes and total number of votes won
	candidate_one_output = (candidate_one + ": " + str(candidate_one_percentage) + "% " + "(" + str(candidate_one_votes) + ")")
	candidate_two_output = (candidate_two + ": " + str(candidate_two_percentage) + "% " + "(" + str(candidate_two_votes) + ")")
	candidate_three_output = (candidate_three + ": " + str(candidate_three_percentage) + "% " + "(" + str(candidate_three_votes) + ")")

	# calculate and create output variables for winner of the election based on popular vote
	if candidate_one_votes > candidate_two_votes and candidate_one_votes > candidate_three_votes:
		winner = candidate_one
	elif candidate_two_votes > candidate_three_votes and candidate_two_votes > candidate_one_votes:
		winner = candidate_two
	else:
		winner = candidate_three
	winner_output = ('Winner: ' + str(winner))

# output to terminal and text file
# create list of outputs
output = [
	header, 
	seperator, 
	total_votes_output,
	seperator,
	candidate_one_output,
	candidate_two_output,
	candidate_three_output,
	seperator,
	winner_output,
	seperator
	]
print('\n')
for line in output:
	print(line)
print('\n')
# map the analysis file and write the file
election_results = os.path.join("analysis", "election_results.txt")
with open(election_results, 'w') as f:
	for line in output:
		f.write(str(line))
		f.write('\n')
