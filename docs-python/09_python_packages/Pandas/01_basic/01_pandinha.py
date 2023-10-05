import pandas as pd

data = [ 10, 20, 30, 40 ]
df = pd.DataFrame(data)

print("-----")
print(df)
print(type(df))
print("-----")

data = { 
    'Name': ['John', 'Tim', 'Rob'],
    'Age': [ 34, 23, 42 ],
    'Salary': [ 3000, 2500, 4000 ]
}

df = pd.DataFrame(data)
print("-----")
print(df)
print(type(df))
print("-----")

print("Then, we notice it's more interesting use a dictionary to create a DataFrame.")