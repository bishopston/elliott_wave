import pandas as pd
import sys

df = pd.read_csv("~/tech_analysis/ew_playground/S&P 500 Historical Data.csv", sep=',',
                encoding="ISO-8859-7", header=0,
                names=['date','close','open','high','low','volume','change'])

#df["close"] = df["close"].values[::-1]
#df = df.sort_index(axis=1 ,ascending=False)
df = df.iloc[::-1]
print(df.head())

df.to_csv('~/tech_analysis/ew_playground/S&P 500 Historical Data_reversed.csv', index=None, sep=',', header=True)