# Dependencies

import os
import csv


# 1 - open the data file
file_to_load = "Resources\election_results.csv"
file_to_save = os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:

    # To do: read and analyze the data here

    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file
    for row in file_reader:
       print(row)
        



#with open(file_to_save, "w") as txt_file:
 #   txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# 2 - Write down the names of the candidates

# 3 - Add a vote count for each candidate

# 4 - Get the total votes for each candidate

# 5 - Get the total votes cast for the election

#txt_file.close()


# close file
# election_data.close()


# How many votes did you get?

# my_votes = int(input("How many votes did you get in the election? "))

# Total votes in teh election

# total_Votes = int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.

# percentage_votes = (my_votes / total_Votes) * 100

# print("I received " + str(percentage_votes)+"% of teh total votes.")

