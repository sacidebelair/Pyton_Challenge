import os
import csv

#This is the path to the file from my deskstop
csvpath = r"/Users/rodiabelair/Desktop/Pyton_Challenge/PyBank/Resources/budget_data.csv"

#this opens the file, scans,prints the header
with open (csvpath) as csvfile:
    csvreader = csv. reader(csvfile, delimiter=',')
    print("Financial Analysis")
    print("----------------------------")

    csv_header = next(csvreader)
    
 
    date =[]
    profit =[]
    #This for loop
    for row in csvreader: 
        date.append(row[0])
        profit.append(int(row[1]))

    print("Total Months:", str(len(date)))

    total =0
    for number in profit:
        total+=number
    print("Total: $",str(total))

    total_change=0
    total_change_list=[]
    for i in range(1,len(profit)):
        total_change+=profit[i]-profit[i-1]
        total_change_list.append(profit[i]-profit[i-1])
    average_change=total_change/(len(profit)-1)
    print("Average Change: $",str(average_change))
    
    
    #taking the max, min, max date, min date from the file
    max_change=max(total_change_list)
    min_change=min(total_change_list)
    max_date=date[total_change_list.index(max_change)+1]
    min_date=date[total_change_list.index(min_change)+1] 
    
    #prints out the results
    print(f"Greatest Increase in Profits: {max_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_change})")
    
    with open("result_PyBank.txt","w") as file:
        file.write("Financial Analysis\n") 
        file.write("----------------------------\n") 
        file.write(f"Total Months: {(len(date))}\n") 
        file.write(f"Total: $ {(total)}\n") 
        file.write(f"Average Change: $ {(average_change)}\n") 
        file.write(f"Greatest Increase in Profits: {max_date} (${max_change})\n") 
        file.write(f"Greatest Decrease in Profits: {min_date} (${min_change})\n") 

