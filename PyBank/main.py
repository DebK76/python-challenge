import os
import csv
csvpath = "./Resources/budget_data.csv"

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

     # Initialize variables
    total_months = 0
    net_profit_loss = 0
    changes = []
    max_increase = ['', 0]
    max_decrease = ['', 0]
    prev_month_profit_loss = None

    # Loop through each row in the CSV file
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        total_months += 1
        net_profit_loss += profit_loss

        # Calculate change in profit/loss from previous month
        if prev_month_profit_loss is not None:
            change = profit_loss - prev_month_profit_loss
            changes.append(change)
            if change > max_increase[1]:
                max_increase = [date, change]
            elif change < max_decrease[1]:
                max_decrease = [date, change]
        prev_month_profit_loss = profit_loss

    # Calculate average change in profit/loss
    avg_change = sum(changes) / len(changes)

    # Print the results
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_profit_loss}')
    print(f'Average Change: ${avg_change:.2f}')
    print(f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})')
    print(f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})')
    




    # Printing the results to terminal
    print ("Financial Analysis")
    print ("--------------------------")
    print(total_months)
    print(profit_loss)
    print(change)
    print(len(changes))
    print(avg_change)
    print(f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})')
    print(f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})')

    # Exporting results to a text file
    with open("Analysis/Pybank.txt", "w") as file_PythonChallenge: 


        file_PythonChallenge.write(f"""Financial Analysis----------------------------------""")

        file_PythonChallenge.write(f'Total Months: {total_months}\n')
        file_PythonChallenge.write(f'Total: ${net_profit_loss}\n')
        file_PythonChallenge.write(f'Average Change: ${avg_change:.2f}\n')
        file_PythonChallenge.write(f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n')
        file_PythonChallenge.write(f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n')