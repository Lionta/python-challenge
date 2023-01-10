import os
import pandas as pd
import csv

#opening the csv file with the data. i have to do it this way, using '..' or not at all just gives me a does not exist error
absolute_path = os.path.dirname(__file__)
file = os.path.join(absolute_path, 'Resources', 'budget_data.csv')

#getting the header
inputFile = csv.reader(file)
header = next(inputFile)
file_df = pd.read_csv(file)

outputAnalysis = open(os.path.join(absolute_path, 'analysis', 'output.txt'),'w')

#figuring out the total months by printing out the number of rows
line1=f"Total Months: {len(file_df)}"
print(line1)
outputAnalysis.write(line1+'\n')


#Total profilt/loss over the entire time period
line2=f"Total: ${file_df['Profit/Losses'].sum()}"
print(line2)
outputAnalysis.write(line2+'\n')

#Average Change
file_df["Difference"] = file_df["Profit/Losses"].diff()
line3=f"Average Change: ${round(file_df['Difference'].mean(),2)}"
print(line3)
outputAnalysis.write(line3+'\n')

#greatest increase
rowNumInc = file_df["Difference"].idxmax()
line4=f"Greatest Increase in Profits {file_df['Date'].iloc[rowNumInc]} (${int(file_df['Difference'].iloc[rowNumInc])})"
print(line4)
outputAnalysis.write(line4+'\n')

#greatest decrease
rowNumDec = file_df["Difference"].idxmin()
line5 = f"Greatest Decrease in Profits: {file_df['Date'].iloc[rowNumDec]} (${int(file_df['Difference'].iloc[rowNumDec])})"
print(line5)
outputAnalysis.write(line5+'\n')

