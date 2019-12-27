import os.path

import csv

candidates = {}
total_votes = 0

csvpath = os.path.join("/Users/ajatashjian/Desktop/python_challenge/03-Python_Homework_PyPoll_Resources_election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    
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
    print(candidate, (votes/total_votes)*100, votes)
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes
print(f"Winner: ", winner)

candidates_lst = {}
for candidate, votes in candidates_lst.items():
    candidates_lst.update(candidate, (votes/total_votes)*100, str(votes))

data_set = ["Total Votes: " + str(total_votes), candidates_lst, "Winner: " + winner]
    
    
file = open('mainpoll.txt', 'w')
for eachitem in data_set:
    file.write(str(eachitem) + '\n')
file.close()

