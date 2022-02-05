# Sports-Reference-App
Repository for Sports Reference's Engineering Internship Prompt

Required packages:
- BeatifulSoup
- pandas

Utilizing BeautifulSoup's web scraping functionality, this script pulls the MLB data from the application website and converts it into a list of lists. Each list entry contains a string version of the data, with whitespace and all html tags removed. The built-in 'remove_tags' method is used to remove the specified tags.

After the raw data list is constructed, a dictionary containing win & loss info is created for each team.

The form of the results dictionary:

Index: Team Name 

Value: A list of dictionaries which contains {Opponent Team Name: [Wins, Losses] list} for each opponent.


The final portion of the code converts the results dictionary into a pandas dataframe which resembles the BaseballRef results matrix. The 'final_results' dataframe is initialized as an empty table with indexes and columns for each team. Iterating over the empty dataframe, the script inputs the number of wins vs. each opponent in each row.

The final results dataframe is printed at the end.
