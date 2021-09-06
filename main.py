# Importing the libraries
import pandas as pd
from igScrap import getFollowers


# Importing the dataset
df = pd.read_csv('res/example.csv')
emails = df.iloc[:, 0].values

resultsFile = 'res/results.csv'



if __name__ == '__main__':
    getFollowers(emails, resultsFile)



