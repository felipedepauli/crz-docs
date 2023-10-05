import pandas as pd

df = pd.read_excel('Pessoas.xlsx')

print(df.head())

ukraines = df.where(df['Pais']=='Ukraine')

print('\n* Ukraines:')
print(ukraines)

print('Notice when we print the Ukraines dataframe, we get a lot of NaN values. This is because the where() method returns a dataframe with the same shape as the original dataframe, but with all the values set to NaN where the condition is not met. To remove the rows with NaN values, we can use the dropna() method.')

ukraines = df.where(df['Pais']=='Ukraine').dropna()

print("----------------")
print(ukraines)

print("Now, we can save the new dataframe to a new Excel sheet.")

eg = df[['Nome', 'Idade']].where(df['Pais']=='Equatorial Guinea').dropna()

print("----------------")
print(eg)


oldies = df[['Pais', 'Idade']].where(df['Idade']>=50).dropna()

print("----------------")
print(oldies)
print(f'{oldies.shape[0]} people are older than 50 years old.')

columbiaOldies = df[['Nome', 'Idade']].where((df['Pais']=='Puerto Rico') & (df['Idade']>=30)).dropna()

print("----------------")
print(columbiaOldies)
