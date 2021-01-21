import os
import csv

# Open and Read CSV
csvpoll = os.path.join("Resources", "election_data.csv")

# reading the header row, printing and setting it aside (Need assitance from mutilpe online sources)
with open(csvpoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_file)

    # Declaring Variables as empty Dictiionaries and lists
    candidates = {}
    count = 0
    votes_cast = 0
    percentvote = 0
    mostvotes = 0
    mostvotenames = ""

    # counting of the votes
    for row in csv_reader:
        candidatevote = row[2]
        count += 1
        # found if online and on someone github (314cascio), the keys functions being used to compare the names in row two and allocate 
        # the right canidate
        if candidatevote in candidates.keys():
            candidates[candidatevote] =+ 1
        else:
            candidates[candidatevote] = 1
    print("Election Results")
    print("-------------------------")
    print("Total Votes: {count}")
    print("-------------------------")


    # Finding the total # votes and casting it to a variable
    for candidatevote in candidates:
        votes_cast =+ candidates[candidatevote]

        # finding the percent for each candidate (using 314cascio code to keep code clean)
        percentvote = (candidates[candidatevote])/(count) * 100
        print(f"{candidates}: {int(percentvote)} % {votes_cast}")

        if candidates[candidatevote] > mostvotes:
            mostvotenames = candidates
            mostvotes = candidates[candidatevote]

    print("-------------------------")
    print(f"WINNER: {mostvotenames}")
    print("-------------------------")




