import os
import csv

# Open and Read CSV
csvpoll = os.path.join("Resources", "election_data.csv")

# reading the header row, printing and setting it aside (Need assitance from mutilpe online sources)
with open(csvpoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_file)

    # Declaring Variables
    candidates = {}
    count = 0
    votes_cast = 0
    percentvote = 0
    mostvotes = 0
    mostvotenames = ""
    
    # counting of the votes
    for row in csv_reader:

        names = row[2]
        count += 1
               
        # found keys() it online and on someones github (314cascio), the keys functions being used to compare the names in row two and allocate 
        # the right canidate
        if names in candidates.keys():
            candidates[names] += 1
        else:
            candidates[names] = 1

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")


    # Finding the total # votes for each canditate
    for names in candidates:
        votes_cast += candidates[names]

        # finding the percent for each candidate (using 314cascio code to keep code clean)
        percentvote = (candidates[names])/(count) * 100
        print(f"{names}: {int(percentvote)}% {votes_cast}")
        
        if candidates[names] > mostvotes:
            mostvotenames = names
            mostvotes = candidates[names]

    print("-------------------------")
    print(f"WINNER: {mostvotenames}")
    print("-------------------------")

#Print text file
with open('poll_results.txt', 'w', newline='') as text:
    text.write("  Election Results""\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(f"Total Votes: {count} \n")
    text.write("----------------------------------------------------------\n\n")
    for names in candidates:
        text.write(f" {names}: {int(percentvote)}% {votes_cast} \n")
    text.write("----------------------------------------------------------\n\n")
    text.write(f"WINNER:  {mostvotenames} \n")
    text.write("----------------------------------------------------------\n")


