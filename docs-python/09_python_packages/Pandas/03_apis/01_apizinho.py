import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/photos'

r = requests.get(url)

data = r.json()


df = pd.DataFrame(data)

print(df.info())
print(df.describe())