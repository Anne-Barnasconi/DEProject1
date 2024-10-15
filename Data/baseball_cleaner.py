import pandas as pd 

# Read file
moneyball = pd.read_csv("baseball_raw.csv")

# Rename column abbreviatons to full names
moneyball.rename(columns={'RS':'Runs_scored',
                     'RA':'Runs_allowed',
                     'W': 'Wins',
                     'OBP': 'On_base_percentage',
                     'SLG': 'Slugging_percentage',
                     'BA':'Batting_average',
                     'G': 'Games_played',
                     'OOBP':'Opponent_on_base_percentage',
                     'OSLG':'Opponent_slugging_percentage',
                    }, inplace=True)

# Compute win percentage statistic
moneyball['Win_percentage'] = moneyball['Wins'] / moneyball['Games_played']

# Set year as categorical variable
moneyball['Year'] = moneyball['Year'].astype('object')

# Drop columns
cols_to_drop = ['Playoffs','RankSeason','RankPlayoffs','Games_played','Wins','Team','Runs_scored','Runs_allowed']
moneyball.drop(labels=cols_to_drop,inplace=True,axis=1)

# Drop rows with NA
moneyball.dropna(inplace=True)

# Encode League variable  
moneyball.loc[moneyball['League'] == 'AL',"League"] = 0
moneyball.loc[moneyball['League'] == 'NL',"League"] = 1

# Encode Decade variable
moneyball['decade60s'] = moneyball['Year'].apply(lambda x: 1 if 1960 <= x < 1970 else 0)
moneyball['decade70s'] = moneyball['Year'].apply(lambda x: 1 if 1970 <= x < 1980 else 0)
moneyball['decade80s'] = moneyball['Year'].apply(lambda x: 1 if 1980 <= x < 1990 else 0)
moneyball['decade90s'] = moneyball['Year'].apply(lambda x: 1 if 1990 <= x < 2000 else 0)
moneyball['decade2000s'] = moneyball['Year'].apply(lambda x: 1 if 2000 <= x < 2010 else 0)
moneyball['decade2010s'] = moneyball['Year'].apply(lambda x: 1 if 2010 <= x < 2020 else 0)
moneyball.drop(labels=['Year'],axis=1,inplace=True)

# Save new data file to csv
moneyball.to_csv("baseball_clean.csv", index=False)