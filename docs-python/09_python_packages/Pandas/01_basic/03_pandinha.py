import pandas as pd

df = {
    'a': [ 10, 20, 30, 40 ],
    'b': [ 100, 200, 300, 400 ],
    'c': [ 1000, 2000, 3000, 4000 ]
}

df = pd.DataFrame(df)

df['sum'] = df['a'] + df['b'] + df['c']

print("-----")
print(df)
print("-----")