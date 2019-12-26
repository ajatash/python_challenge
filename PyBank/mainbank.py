import os.path

import csv

months = []
pnl = []

csvpath = os.path.join("/Users/ajatashjian/Desktop/python_challenge/03-Python_Homework_PyBank_Resources_budget_data.csv")


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    for row in csvreader:
        months.append(row[0])
        pnl.append(int(row[1]))
        
print(f"Total Months: ", len(months))
print(f"Total: $", sum(pnl))


change = []
for n in range(1, len(pnl)):
  change.append(pnl[n] - pnl[n-1])
  
print(f"Average Change: ", sum(change)/len(change))
maxincrease = max(change)
maxmonth = change.index(maxincrease)
Greatmonth = months[maxmonth +1]

minincrease = min(change)
minmonth = change.index(minincrease)
Smallmonth = months[minmonth +1]

print(f"Greatest Increase in Profits: ", Greatmonth, " $", maxincrease)
print(f"Greatest Decrease in Profits: ", Smallmonth, " $", minincrease)
    
        
    

    
    
    

