import pandas as pd
'''z=['DEEP', 'LEARNING', 'IS', 'FUN']
s=pd.Series(z,index=['a', 'b', 'c', 'd'])
s['a'] = 'MACHINE'
# print(s.loc['b'])
# print(s)

x={'day1':2100, 'day2':2200, 'day3':2300}
xseries=pd.Series(x)
# print(xseries[xseries > 2150])

# dataframe

data={'calories':[2100, 2200, 2300], 'duration':[30, 45, 60]}
df=pd.DataFrame(data,index=['day1', 'day2', 'day3'])

# adding new coloumn?
df['job']=['deep', 'learning', 'fun']

# addingg a new row?
nrow={'calories':2400, 'duration':90, 'job':'python'}
df=pd.concat([df, pd.DataFrame(nrow, index=['day4'])])
print(df)
'''


print("Reading CSV now...")

op = pd.read_csv('op.csv',index_col='Name')


# SELECTION

# print(op)
print(op['Name'])
# print(op.loc['Luffy'])
# print(op['Devil_Fruit'])