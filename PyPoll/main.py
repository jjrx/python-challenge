# dependences
import pandas as pd

# import csv file
file = "Resources/election_data.csv"
election_df = pd.read_csv(file)

# calculate total number of votes
total_votes = election_df["Voter ID"].count()

# create a list of candidates
candidates = election_df["Candidate"].unique().tolist()

# determine the number of votes per candidate
votes_per_candidate = election_df["Candidate"].value_counts()

# print out results
largest_num_of_votes = 0
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# for each candidate, display their raw number of votes and their percent of total votes
for candidate in candidates:
    num_of_votes = votes_per_candidate[candidate]
    percent_of_votes = (num_of_votes/total_votes) * 100
    # determine the winner by keeping track of which candidate has the largest number of votes
    if num_of_votes > largest_num_of_votes:
        largest_num_of_votes = num_of_votes
        # set the winner variable equal to this candidate since they currently have the most votes
        winner = candidate 
    print(f"{candidate}: {percent_of_votes:.3f}% ({num_of_votes})")   
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

