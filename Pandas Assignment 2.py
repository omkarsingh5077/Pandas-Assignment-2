import pandas as pd
import numpy as np

users= pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',index_col='user_id',sep='|')

print(users.head(10))

print(users.tail(10))

print(users.info())

print(users.shape)

print(users.shape[1])

print(users.head(0))

print(users.index)

print(users.dtypes)

print(users.occupation)

print(users.groupby(by='occupation').occupation.count())

print(users.occupation.value_counts().head(1).index[0])

print(users.describe())

print(users.describe(include="all"))

print(users.occupation.describe())

print(round(users.age.mean()))

# print(users.age.value_counts().tail())