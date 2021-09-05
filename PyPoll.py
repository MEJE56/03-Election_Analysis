# The data to be retrived:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Assign a variable to load the file from a path 
file_to_load = os.path.join("Resources", "election_results.csv") 
# Assign a variable to save file Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize a variable to accumulate total number of votes
total_votes=0
# Empty list: Candidate Options
candidate_options = []
# Empty dicitinary: Votes cast for each candidate
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)    
    # Read and print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Counter: Add to the total vote count
        total_votes += 1
        
        # Get candidate name from each row 
        candidate_name = row[2]
        
        
        # If the candidate has not been added to candidate option: meaning does not match any existing candidate
        if candidate_name not in candidate_options: 
            #Adding candidate name to the list of cadidates
            candidate_options.append(candidate_name)
            # Initialize variable to track candidate's vote count
            candidate_votes[candidate_name] = 0
        # Counter: Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the audit elections results to our a text
with open(file_to_save, "w") as txt_file:

    # Assign a variable: save the final vote count
    election_results = (
        f"\nElection Results\n"
        f"----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------\n")
    
    # Print in terminal the final vote count
    print(election_results, end="")

    # Save the final vote count in the .txt file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count for a candidate
        votes = candidate_votes[candidate_name]
    
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
    
        # Assign a variable: save each candidate name and percentage of votes
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print in the terminal each candidate name and percentage of votes    
        print(candidate_results)

        # Save the candidate name and percentage of votes in the .txt file
        txt_file.write(candidate_results)
    
        # Determine winning vote count and candidate
        # Assess if votes for a candidate are greater than the winning count
        if (votes > winning_count) & (vote_percentage > winning_percentage):
            # If votes and % greater than winning votes and %, assign winnig_count and winning percentage with votes and vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Assign a variable: save the winning candidate summary
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    # Print in terminal the winning candidate summary
    print(winning_candidate_summary)
    # Save the winning candidate summary in the .txt file
    txt_file.write(winning_candidate_summary)