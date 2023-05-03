import os
import csv
csvpath = "./Resources/election_data.csv"

with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds the following contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ['', 0]

    # Loop through each row in the CSV file
    for row in csvreader:
        candidate = row[2]
        total_votes += 1

        # Add candidates to dictionary if they have'nt been seen before
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

        # Check if candidate has more votes than current winner
        if candidates[candidate] > winner[1]:
            winner = [candidate, candidates[candidate]]

    # Print these results to terminal
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'-------------------------')
    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        print(f'{candidate}: {percentage:.3f}% ({votes})')
    print(f'-------------------------')
    print(f'Winner: {winner[0]}')
    print(f'-------------------------')



    # Export the following results to a text file
    with open("Analysis/PyPoll.txt", "w") as file_PythonChallenge:

        
        file_PythonChallenge.write(f'Election Results\n')
        file_PythonChallenge.write(f'-------------------------\n')
        file_PythonChallenge.write(f'Total Votes: {total_votes}\n')
        file_PythonChallenge.write(f'-------------------------\n')
        for candidate, votes in candidates.items():
            percentage = votes / total_votes * 100
            file_PythonChallenge.write(f'{candidate}: {percentage:.3f}% ({votes})\n')
        file_PythonChallenge.write(f'-------------------------\n')
        file_PythonChallenge.write(f'Winner: {winner[0]}\n')
        file_PythonChallenge.write(f'-------------------------\n')