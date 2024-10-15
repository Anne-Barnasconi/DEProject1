import pandas as pd 
from sklearn.model_selection import train_test_split

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


# Set year as categorical variable
moneyball['Year'] = moneyball['Year'].astype('object')

# Drop columns
cols_to_drop = ['RankSeason','RankPlayoffs','Games_played','Wins','Team','Runs_scored','Runs_allowed','Year','League']
moneyball.drop(labels=cols_to_drop,inplace=True,axis=1)

# Drop rows with NA
moneyball.dropna(inplace=True)

# Split train and test set
training, prediction = train_test_split(moneyball, test_size=0.10)

# Save new data file to csv
training.to_csv("training_set_moneyball.csv", index=False)
prediction.to_csv("prediction_set_moneyball.csv", index=False)

