# Import the operating system and csv modules
import os
import csv

print("Election Results")
print("------------------------")

# map the resource file
election_data = os.path.join("Resources", "election_data.csv")

# read the CSV file and store in csvreader
with open(election_data) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	# store and skip the column headers
	csv_header = next(csvreader)

	#define variables


	# convert data to list of dictionaries
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

	# calculate total number of votes each candidate won
	candidates_set = set(candidates)
	candidate_one = list(candidates_set)[0]
	candidate_two = list(candidates_set)[1]
	candidate_three = list(candidates_set)[2]
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
	

	# calculate and display total number of votes
	total_votes = (len(election_data))
	print(f"Total Votes:", + total_votes)
	print("------------------------")

	# calculate percentage of votes each candidate won
	candidate_one_percentage = (candidate_one_votes / total_votes) * 100
	candidate_one_percentage = round(candidate_one_percentage, 3)
	candidate_two_percentage = (candidate_two_votes / total_votes) * 100
	candidate_two_percentage = round(candidate_two_percentage, 3)
	candidate_three_percentage = (candidate_three_votes / total_votes) * 100
	candidate_three_percentage = round(candidate_three_percentage, 3)

	# display candidate name, percentage vootes and total number of votes each candidate won
	print(candidate_one + ": " + str(candidate_one_percentage) + "% " + "(" + str(candidate_one_votes) + ")")
	print(candidate_two + ": " + str(candidate_two_percentage) + "% " + "(" + str(candidate_two_votes) + ")")
	print(candidate_three + ": " + str(candidate_three_percentage) + "%" + "(" + str(candidate_three_votes) + ")")

	# calculate and display winner of the election based on popular vote
	if candidate_one_votes > candidate_two_votes and candidate_one_votes > candidate_three_votes:
		winner = candidate_one
	elif candidate_two_votes > candidate_three_votes and candidate_two_votes > candidate_one_votes:
		winner = candidate_two
	else:
		winner = candidate_three
	print("------------------------")
	print(f"Winner: ", winner)
	print("------------------------")
