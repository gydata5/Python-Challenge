# Import necessary modules
import csv
import os

# Constants
INPUT_PATH = os.path.join("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("analysis", "election_analysis.txt")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(INPUT_PATH) as election_data_file:
    reader = csv.reader(election_data_file)

    # Read the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        # Get the candidate's name from the row
        candidate_name = row[2]
        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Print the total vote count (to terminal)
election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

# Loop through the candidates to determine vote percentages and identify the winner
for candidate in candidate_votes:
    # Get the vote count and calculate the percentage
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes)*100

    # Update the winning candidate if this one has more votes
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate

    # Print and save each candidate's vote count and percentage
    election_results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

# Generate and print the winning candidate summary
election_results += (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")

with open(OUTPUT_PATH, "w") as txt_file:
    txt_file.write(election_results)
    print(election_results, end="")