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

        candidatenames = row[2]
        count += 1
        # found if online and on someone github (314cascio), the keys functions being used to compare the names in row two and allocate 
        # the right canidate
        if candidatenames in candidates.keys():
            candidates[candidatenames] =+ 1
        else:
            candidates[candidatenames] = 1


    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")


    # Finding the total # votes and casting it to a variable
    for candidatenames in candidates:
        votes_cast =+ candidates[candidatenames]

        # finding the percent for each candidate (using 314cascio code to keep code clean)
        percentvote = (candidates[candidatenames])/(count) * 100
        print(f"{candidates}: {int(percentvote)} % {votes_cast}")

        if candidates[candidatenames] > mostvotes:
            mostvotenames = candidatenames
            mostvotes = candidates[candidatenames]

    print("-------------------------")
    print(f"WINNER: {mostvotenames}")
    print("-------------------------")




