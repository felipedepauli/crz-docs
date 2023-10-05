import pandas as pd
from pandasql import sqldf

def pysqldf(q):
    return sqldf(q, globals())

df_people = pd.read_excel('./Pessoas.xlsx')

print(df_people.head())

result = pysqldf('''
    SELECT Nome, Idade FROM df_people
    WHERE Idade > 30             
    ORDER BY Idade DESC
''')

print(result)