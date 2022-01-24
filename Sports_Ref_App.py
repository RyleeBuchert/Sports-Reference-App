# Rylee Buchert
# January 21, 2022
# Sports Ref Internship App Question 2

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

# function to remove html tags from a string
def remove_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

if __name__ == "__main__":

    # scrape html data and clean with bs4
    url = 'https://sports-reference-llc.breezy.hr/p/a00e207e458f-sports-reference-2022-summer-internship'
    url_request = requests.get(url)
    sports_ref_soup = BeautifulSoup(url_request.text, 'lxml')
    sports_ref_data = [remove_tags(str(line)).strip(' ') for line in sports_ref_soup.find_all("p")[40:112]]

    # create results dictionary from web data
    team_stack = []
    results_dict = {}
    opponent_list = []
    for line in sports_ref_data:
        if line[0] == "}":
            # creates dict entry:  {      team name      : [{ opponent name: [    wins vs opponent      ,       losses vs opponent        ]}    for each opponent    ]}            
            results_dict.update(   {team_stack.pop()[1:4]: [{opp[1:4]: [opp[14:16].strip(' ').strip(','), opp[23:25].strip(' ').strip(',')]} for opp in opponent_list]})
            opponent_list = []
        elif len(line) < 10:
            team_stack.append(line)
        else:
            opponent_list.append(line)

    # create final results dataframe from dictionary
    team_list = list(results_dict.keys())
    final_results = pd.DataFrame(columns = team_list, index = team_list)
    for index in final_results._stat_axis.values:
        for col in final_results.columns:
            if index == col:
                final_results.loc[index][col] = '--'
            else:
                # finds index of results_dict entry where wins vs opponent iterable is stored
                list_key = [i for i in range(len(results_dict[index])) if list(results_dict[index][i].keys())[0] == col][0]
                final_results.loc[index][col] = int(results_dict[index][list_key][col][0])

    # print final baseball results
    print(final_results)