import csv
import os

# Path to collect data from the Resources folder
file_to_load = os.path.join('Resources', 'election_data.csv')
# Path to save the analysis results
file_to_save = os.path.join('analysis', 'election_results.txt')

# Initialize a total vote counter and a dictionary for candidate votes
total_votes = 0
candidate_votes = {}

# Open the election data file and read it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header row
    headers = next(reader)

    # Loop through each row in the CSV
    for row in reader:
        total_votes += 1
        candidate_name = row[2]

        # If the candidate does not match any existing candidate, add to the candidate list
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Save the results to a text file and print them to the terminal
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal and write to the text file
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    winner = max(candidate_votes, key=candidate_votes.get)

    # Loop through the candidate list
    for candidate in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

        # Print each candidate's voter count and percentage to the terminal and write to the text file
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Print the winner of the election to the terminal and write to the text file
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
