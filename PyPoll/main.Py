import os
import csv

#This is the path to the file from my deskstop
csvpath = r"/Users/rodiabelair/Desktop/Pyton_Challenge/PyPoll/Resources/election_data.csv"

#this opens the file, scans,prints the header
with open (csvpath) as csvfile:
    csvreader = csv. reader(csvfile, delimiter=',')
    print("Election Results")
    print("----------------------------")

    csv_header = next(csvreader)
    
 
    vote_id =[]
    county =[]
    candidate =[]
    #This for loop
    for row in csvreader: 
        vote_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    print(f"Total Votes: {len(vote_id)}")
    print("----------------------------")

    candidate_list=list(set(candidate))
    Charles=0
    Diana=0
    Raymon=0
    for person in candidate:
        if person == "Raymon Anthony Doane":
            Raymon += 1
        elif person == "Charles Casper Stockham":
            Charles += 1
        elif person == "Diana DeGette":
            Diana += 1

    print(f"Charles Casper Stockham: {Charles/len(vote_id)*100:.3f}% ({Charles})")
    print(f"Diana DeGette: {Diana/len(vote_id)*100:.3f}% ({Diana})")
    print(f"Raymon Anthony Doane: {Raymon/len(vote_id)*100:.3f}% ({Raymon})")
    print("----------------------------")
    print("Winner: Diana DeGette")
    print("----------------------------")

    with open("result_PyPoll.txt","w") as file:
        file.write("Election Results\n")
        file.write("----------------------------\n")
        file.write(f"Total Votes: {len(vote_id)}\n")
        file.write("----------------------------\n")
        file.write(f"Charles Casper Stockham: {Charles/len(vote_id)*100:.3f}% ({Charles})\n")
        file.write(f"Diana DeGette: {Diana/len(vote_id)*100:.3f}% ({Diana})\n")
        file.write(f"Raymon Anthony Doane: {Raymon/len(vote_id)*100:.3f}% ({Raymon})\n")
        file.write("----------------------------\n")
        file.write("Winner: Diana DeGette\n")
        file.write("----------------------------\n")