import pandas as pd


df = pd.DataFrame(
    [
        [ 10, 20, 30, 40 ],
        [ 100, 200, 300, 400 ],
        [ 1000, 2000, 3000, 4000 ]
    ], columns=['A', 'B', 'C', 'D']
)

print("-----")
print(df)
print("-----")

df = df.drop(1)
print("-----")
print(df)
print("-----")

df = pd.DataFrame(
    {
        'A': [ 10, 20, 30, 40 ],
        'B': [ 100, 200, 300, 400 ],
        'C': [ 1000, 2000, 3000, 4000 ]
    }
)

df = df.drop(1)

print("-----")
print(df)
print("-----")


df = pd.DataFrame(
    [
        [ 10, 20, 30, 40 ],
        [ 100, 200, 300, 400 ],
        [ 1000, 2000, 3000, 4000 ]
    ], columns=['A', 'B', 'C', 'D']
)

df = df.drop('B', axis=1)
print("-----")
print(df)
print("-----")