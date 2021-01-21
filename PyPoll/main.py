import os
import csv

#Open and Read CSV
csvpoll = os.path.join("Resources", "election_data.csv")

#reading the header row, printing and setting it aside (Need assitance from mutilpe online sources)
with open(csvpoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_file)

    #Declaring Variables
    votecount = []
    totalvotecount = 0
    candidateslist = []
    named_candidate_list = []
    votepercent = []

    #Starting count
    for row in csv_reader:
        #total number of votes
        totalvotecount = totalvotecount + 1
        #Set Candidates to a list
        candidateslist.append(row[2])
        #Find the unique names (shrawantee github)

    for x in set(candidateslist):
        named_candidate_list.append(x)
        # v is the total number of votes
        v = candidateslist.count(x)
        votecount.append(v)
        #p is finding the percentage
        p = (v/totalvotecount)*100
        votepercent.append(p)

        




