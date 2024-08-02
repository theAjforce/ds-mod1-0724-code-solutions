import pandas as pd
import numpy as np

cars = pd.read_csv("mtcars.csv")
beer = pd.read_fwf("beer.txt")
nhl = pd.read_excel("NHL 2015-16.xlsx")

cars.to_csv("new_mtcars.csv")
beer.to_csv("new_beer.txt")
nhl.to_excel("new nhl 2015-2016.xlsx")

def file_checker(df):
    last_let = df[-1]
    if last_let in df == 'x':
        dataframe = pd.read_excel(df)
    else:
        dataframe = pd.read_csv(df)
    return dataframe
