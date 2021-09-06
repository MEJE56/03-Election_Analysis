# -*- coding: UTF-8 -*-
"""Election Analysis with PyPoll"""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_turnout = ""
county_turnout_count = 0
county_turnout_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in county_options:


            # 4b: Add the existing county to the list of counties.
            county_options.append(county)

            # 4c: Begin tracking the county's vote count.
            county_votes[county] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary
    # Determine the percentage of votes for each county by looping through the counts
    # Iterate through the candidate list
    for county in county_votes:
        # 6b: Retrieve the county vote count
        county_voter = county_votes[county]
    
        # 6c: Calculate the percentage of votes for the county
        county_percentage = float(county_voter) / float(total_votes) * 100
    
        # 6d: Print the county results to the terminal
        # Assign a variable: save each county, votes and percentage of votes
        county_results = (
            f"{county}: {county_percentage:.1f}% ({county_voter:,})\n")
        
        # Print in the terminal each county, votes and percentage of votes   
        print(county_results)

        # 6e: Save the county votes to a text file.
        # Save the candidate name and percentage of votes in the .txt file
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        # Determine county with largest turnout percentage
        # Assess if votes for each county are greater than the county turnout count
        if (county_voter > county_turnout_count) & (county_percentage > county_turnout_percentage):
            # If votes and % greater than county votes and %, assign votes and county percentage to county turnout count and county turnout percentage 
            county_turnout_count = county_voter
            county_turnout_percentage = county_percentage
            largest_county_turnout = county

    # 7: Print the county with the largest turnout to the terminal.
    # Assign a variable: save the county with the largest turnout
    largest_turnout_county_summary = (
        f"-------------------------\n"
        f"Largest Couty Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    # Print in terminal the county with the largest turnout
    print(largest_turnout_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    # Save the county with the largest turnout in the .txt file
    txt_file.write(largest_turnout_county_summary)

    # Save the final candidate vote count to the text file.
    # Determine the percentage of votes for each candidate by looping through the counts by iterating through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count for a candidate
        votes = candidate_votes.get(candidate_name)
        # Calculate the percentage of votes for the candidate
        vote_percentage = float(votes) / float(total_votes) * 100
        # Assign a variable: save candidate name, votes and percentage of votes
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print in the terminal candidate name, votes and percentage of votes 
        print(candidate_results)
        # Save the candidate name, votes and percentage of votes in the .txt file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Assess if votes for a candidate are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If votes and votes % greater than winning votes and winning %, assign votes and vote_percentage to winnig_count and winning_percentage 
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Assign a variable: save the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Print in terminal the winning candidate summary
    print(winning_candidate_summary)

    # Save the winning candidate summary to the .txt file
    txt_file.write(winning_candidate_summary)
