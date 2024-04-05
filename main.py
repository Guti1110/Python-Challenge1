import os
import csv

# File path for the CSV file
file_path = os.path.join("Resources", "election_data.csv")

# Open the CSV file and read it
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = list(reader)

# votes cast
total_votes = len(data)

# place to store results
results = {}

# Count votes for each candidate
for row in data:
    candidate = row[2]  
    if candidate in results:
        results[candidate] += 1
    else:
        results[candidate] = 1

# percentage of votes for each candidate
for candidate, votes in results.items():
    percentage = (votes / total_votes) * 100
    results[candidate] = {'votes': votes, 'percentage': percentage}

# Find the winner
max_votes = 0
winner = ""
for candidate, votes in results.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, info in results.items():
    print(f"{candidate}: {info['percentage']:.3f}% ({info['votes']})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
#i used class activitities and chatgpt for reference and in order to be able to finish the challenge but for some reason it doesn't do what i want when looking for the csv file