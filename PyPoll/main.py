import os
import csv

#Open and Read CSV
csvpoll = os.path.join("Resources", "election_data.csv")

#reading the header row, printing and setting it aside (Need assitance from mutilpe online sources)
with open(csvpoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_file)

    #Declaring Variables
    votes = []
    totalvotes = 0
    candidateslist = ""


