import pandas as pd


df = {
    'Name': ['John', 'Tim', 'Rob'],
    'Age': [ 34, 23, 42 ],
    'Salary': [ 3000, 2500, 4000 ]
}

df = pd.DataFrame(df)

print("-----")
print(df)
print("-----")
print(df.iloc[0])
print("-----")
print(df.iloc[1])
print("-----")
print(df.iloc[2])
print("-----")

print(df.iloc[0:2])
print("-----")


print("Then, we can use the iloc method to get the data from a specific row.")