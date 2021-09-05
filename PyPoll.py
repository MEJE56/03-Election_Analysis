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


# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    
    
    
    
    
    
    # print(election_data)




# ***how to write



# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")