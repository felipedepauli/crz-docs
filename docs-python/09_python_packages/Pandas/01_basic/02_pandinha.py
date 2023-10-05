import pandas as pd

df = {
    'UNITS': [ 10, 20, 30, 40 ],
    'COST': [ 100, 200, 300, 400 ],
    'PROFIT': [ 1000, 2000, 3000, 4000 ]
}

df = pd.DataFrame(df)

print("-----")
print(df)
print(type(df))
print(type(df['UNITS']))
print("-----")

df = {
    'UNITS': pd.Series([ 10, 20, 30, 40 ]),
    'COST': pd.Series([ 100, 200, 300, 400 ]),
    'PROFIT': pd.Series([ 1000, 2000, 3000, 4000 ])   
}

df = pd.DataFrame(df)

print("-----")
print(df)
print(type(df))
print(type(df['UNITS']))
print("-----")


print("Then we can notice after create the pandas, a list will be a pd.Series and a dictionary will be a pd.DataFrame.")