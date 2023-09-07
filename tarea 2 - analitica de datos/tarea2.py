import pandas as pd

url ="C:/Users/Aio5/Downloads/wine/wine.data"

Data = pd.read_csv(url, sep=',', header=None)

Data.head()

Data.describe()