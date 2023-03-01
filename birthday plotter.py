'''
Calculates how likely it is, to have multiple people with the same birthday in the same group
'''
import csv
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

#https://pythonprogramming.net/loading-file-data-matplotlib-tutorial/
'''
with open('Simple Birthday.csv') as csvdile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
'''

#https://stackoverflow.com/a/57579621/5531122
df = pd.read_csv('Simple Birthday.csv', header=None)

#https://stackoverflow.com/a/21165116/5531122
#boolean Series indicating which columns have nonzero entries
#print((df != 0).any(axis=0))

#delete columns with only zeros
df = df.loc[:, (df != 0).any(axis=0)]

#Name columns by the repeating 
'''
names = []
for i in range(2,len(df.columns)+2):
	names.append(str(i))
'''
#Column names indicating number of people with the same birth date
names = range(2,len(df.columns)+2)
df.columns = names
print(df.columns)

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.divide.html
#df_new = df[3].div(2/3)

df_calc = df.copy()
for i in names:
	df_calc[i] = df_calc[i].div(2/i)
#print(df_calc.sum(axis=1))
#print('new',df_calc)
#print('old',df)

#Adding calculation of likeliness of two people haveing the same birthday
df['Repeat'] = df_calc.sum(axis=1)

#https://stackoverflow.com/a/32249984/5531122
#change index to be in line with population
df.index = df.index + 2

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Likelyhood of repeating Birthdays')

ax1.plot(df)
ax2.plot(df)
ax2.set_yscale('log')
ax1.legend(df)
ax2.legend(df)
ax1.set_ylabel('Population')
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Population')
plt.show()


