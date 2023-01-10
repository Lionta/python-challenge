import os
import pandas as pd
import csv

#opening the csv file with the data. i have to do it this way, using '..' or not at all just gives me a does not exist error
absolute_path = os.path.dirname(__file__)
file = os.path.join(absolute_path, 'Resources', 'election_data.csv')

#getting the header
inputFile = csv.reader(file)
header = next(inputFile)
file_df = pd.read_csv(file)

#starting a working file for output
outputAnalysis = open(os.path.join(absolute_path, 'analysis', 'output.txt'),'w')

linebreak = "-------------------------"
print("Election Results")
outputAnalysis.write("Election Results\n")

#calculating total votes by counting the number of lines
print(linebreak)
print(f"Total Votes: {len(file_df)}")
outputAnalysis.write(linebreak+"\n")
outputAnalysis.write(f"Total Votes: {len(file_df)}\n")


print(linebreak)
outputAnalysis.write(linebreak+"\n")

#finding the number of votes per candidate, and setting up variables to find who had the most votes and store the result
numVotes = file_df['Candidate'].value_counts()
mostVotes = 0
winner = ""

#looping through the series returned by value_counts() and printing out the names, vote count and percentage of votes
for names, votes in numVotes.items():
    print(f"{names}: {round((votes/len(file_df))*100,3)}% ({votes})")
    outputAnalysis.write(f"{names}: {round((votes/len(file_df))*100,3)}% ({votes})\n")
    #if the current amonut of votes is more than the historical max, then it changes the max and changes the winners name. 
    if(votes>mostVotes):
        mostVotes = votes
        winner = names

#displaying the winner
print(linebreak)
print(f"Winner: {winner}")
outputAnalysis.write(linebreak+"\n")
outputAnalysis.write(f"Winner: {winner}")