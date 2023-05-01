import os
import csv
csvpath ="C:/Users/debbi/OneDrive/Documents/GitHub/python-challenge/Resources/budget_data.csv"

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    sum_months = 0
    for row in csvreader:
        #print(f"date = {row[0]}") 
        #print(f"profit/losses = {row[1]}") 
        # adding 1 for reach row  to the sum_months number assuming each row is a month
        sum_months = sum_months + 1
        print(f"total number of months = {sum_months}")

        #Question 2

        with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
            csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    total_profit_loss = 0
    #converting profit/loss string to an integer
    print(f"date = {row[0]}")
    print(f"the net total profit/losses = {row[1]}")
   
