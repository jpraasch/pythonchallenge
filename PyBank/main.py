import os
import csv

#Open and Read CSV
csvbank = os.path.join("Resources", "budget_data.csv")


with open(csvbank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
   #Need to skip header (Thanks ravikanth-kolla github)
    next(csv_reader)

    #Delecaring Variables
    total_months = []
    total_revenues = []
    Difference = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""

    for row in csv_reader:
        total_months.append(row[0])
        total_revenues.append(int(row[1]))

    #Print out Analysis
    print("Financial Analysis")
    print("---------------------------------------------------------------------")
    #total months
    print("Total Months: ", len(total_months))
    #Total ($)
    print("Total: $ ", sum(total_revenues))


    for i in range (1, len(total_revenues)):

        #Average change between months sent to a list
        Difference.append(total_revenues[i] - total_revenues[i-1])

        #Average of the values
        AvgChange = sum(Difference)/len(Difference)

        #Find the greatest Increase
        Greatest_Increase = max(Difference)
        Greatest_Increase_Date = str(total_months[Difference.index(max(Difference))])

        #find greatest decrease
        Greatest_Decrease = min(Difference)
        Greatest_Decrease_Date= str(total_months[Difference.index(min(Difference))])

    #total average change ($0)
    print ("Average Change: $", round(AvgChange))
    #Greatest Increase in Profits (Month-Year Amount)
    print("Greatest Increase: ", Greatest_Decrease_Date, "($", Greatest_Increase, ")")
    #Greats Decreas in Profits (See above)
    print("Greatest Decrease: ", Greatest_Decrease_Date, "($", Greatest_Decrease, ")")

#Print text file
with open('financial_analysis.txt', 'w', newline='') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(len(total_months)) + "\n")
    text.write("    Total Profits: " + "$" + str(sum(total_revenues)) +"\n")
    text.write("    Average Change: " + '$' + str(round(AvgChange)) + "\n")
    text.write("    Greatest Increase in Profits: "+ Greatest_Decrease_Date + "($"+ str(Greatest_Increase) + ")\n")
    text.write("    Greatest Decrease in Profits: "+ Greatest_Decrease_Date + " ($"+ str(Greatest_Decrease) + ")\n")
    text.write("----------------------------------------------------------\n")