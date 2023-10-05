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

df = df.append({'Name': 'Paul', 'Age': 32, 'Salary': 5000}, ignore_index=True)

print("-----")
print(df)
print("-----")

new_row = pd.DataFrame({'Name': ['Felipe'], 'Age': [40], 'Salary': [15000]})
df = pd.concat([df, new_row])

print("-----")
print(df)
print("-----")

print("It doesn't work right because the index is not being ignored.")

df = df.drop(3)

df = pd.concat([df, new_row], ignore_index=True)

print("-----")
print(df)
print("-----")

print("Now, it works right because the index is being ignored.")