import os.path

import csv

months = []
pnl = []

csvpath = os.path.join("/Users/ajatashjian/Desktop/python_challenge/03-Python_Homework_PyBank_Resources_budget_data.csv")


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    
    for row in csvreader:
        months.append(row[0])
        pnl.append(int(row[1]))
total_mos = len(months)
total_pnl = sum(pnl)
print(f"Total Months: ", total_mos)
print(f"Total: $", total_pnl)



change = []
for n in range(1, len(pnl)):
  change.append(pnl[n] - pnl[n-1])
avg_change = sum(change)/len(change)
print(f"Average Change: ", avg_change)
maxincrease = max(change)
maxmonth = change.index(maxincrease)
Greatmonth = months[maxmonth +1]

minincrease = min(change)
minmonth = change.index(minincrease)
Smallmonth = months[minmonth +1]

print(f"Greatest Increase in Profits: ", Greatmonth, " $", maxincrease)
print(f"Greatest Decrease in Profits: ", Smallmonth, " $", minincrease)


data_list = ["Total Months: " + str(len(months)), "Total: $" + str(total_pnl), "Average Change: " + str(avg_change), "Greatest Increase in Profits: " + Greatmonth + " $" + str(maxincrease), "Greatest Decrease in Profits: " + Smallmonth + " $" + str(minincrease)]

file = open('mainbank.txt', 'w')
for eachitem in data_list:
    file.write(str(eachitem) + '\n')
file.close()


    
    
    

