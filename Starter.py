import pandas as pd

train = pd.read_csv("/Users/scobra/Documents/Kaggle/Sberbank-Russian-Housing-Market/train.csv")
macro = pd.read_csv("/Users/scobra/Documents/Kaggle/Sberbank-Russian-Housing-Market/macro.csv")

train.describe()
