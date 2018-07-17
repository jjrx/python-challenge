# dependences
import pandas as pd
import os

# import csv file
file = "Resources/election_data.csv"
election_df = pd.read_csv(file)

# calculate total number of votes
total_votes = election_df["Voter ID"].count()

# create a list of candidates
candidates = election_df["Candidate"].unique().tolist()

# determine the number of votes per candidate
votes_per_candidate = election_df["Candidate"].value_counts()

# create a dictionary where keys are candidate names and values are a list of candidate's total votes and percent votes
candidates_dict = {}
for candidate in candidates:
    candidates_dict[candidate] = []
    # add raw votes per candidate to list
    candidates_dict[candidate].append(votes_per_candidate[candidate])
    # add percent votes to list
    candidates_dict[candidate].append((votes_per_candidate[candidate]/total_votes) * 100)

# determine the winner by iterating over the candidates dictionary and keeping track of which candidate has the most votes
largest_num_of_votes = 0
for candidate in candidates_dict:
    # first item in each key list is the number of votes
    if candidates_dict[candidate][0] > largest_num_of_votes:
        largest_num_of_votes = candidates_dict[candidate][0]
        winner = candidate

# display results in .txt file
output_file = os.path.join("Resources", "PyPoll_Results.txt")
with open(output_file, "w") as datafile:
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Total Votes: {total_votes}\n")
    datafile.write("----------------------------\n")
    for key in candidates_dict:
        datafile.write(f"{key}: {candidates_dict[key][1]:.3f}% ({candidates_dict[key][0]})\n")
    datafile.write("----------------------------\n")
    datafile.write(f"Winner: {winner}\n")
    datafile.write("----------------------------\n")

# print out contents of .txt file in terminal
with open(output_file, "r") as f:
    results = f.read()
    print(results)
