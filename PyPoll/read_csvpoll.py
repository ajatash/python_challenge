import os.path

import csv

candidates = {}
total_votes = 0

csvpath = os.path.join("/Users/ajatashjian/Desktop/python_challenge/03-Python_Homework_PyPoll_Resources_election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
print(f"Total Votes: ", total_votes)
winner = ""
winning_votes = -1
for candidate, votes in candidates.items():
    print(candidate, votes, (votes/total_votes)*100)
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
print(f"Winner: ", winner)
    

