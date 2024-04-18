### Election Analysis Script
This script processes voting data from a CSV file to calculate the total number of votes each candidate received and determines who the winner of the election is. Here's what it does step-by-step:

#### Reads a CSV File:
It opens a CSV file where each row represents a vote for a candidate.
#### Counts Votes:
As it reads through each row, it counts the total number of votes and also keeps track of how many votes each candidate receives.
#### Calculates Percentages:
For each candidate, it calculates what percentage of the total votes they received.
#### Determines the Winner:
After all votes are counted and percentages are calculated, it identifies which candidate has the highest number of votes.
#### Outputs Results:
Finally, it prints out the results to the terminal and also writes them to a text file. This includes the total votes, votes per candidate, their percentages, and the winner of the election.


### Financial Data Analysis Script
This script analyzes financial data from a CSV file to report on overall financial performance over time. Here's the breakdown of its operations:

#### Opens and Reads a CSV File:
Similar to the first script, it reads from a CSV file, but this time each row contains a date and a profit/loss value for a month.
#### Tracks Financial Totals and Changes:
As it processes each row, it updates the total months recorded, the cumulative profit/loss, and calculates the change in profit/loss from the previous month.
#### Identifies Extremes:
While processing, it checks for the greatest increase in profits and the greatest decrease in losses, keeping track of when these occurred.
#### Calculates Averages:
After processing all rows, it calculates the average change in profit/loss over the entire period.
#### Outputs a Summary:
Finally, it prints and writes out a financial summary to the terminal and a text file, detailing the total months, total profit/loss, average change, and the points of greatest increase and decrease in profits.