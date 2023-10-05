import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./banknotes.csv')

print(df.head())
df.info()
print(df.describe())

sns.pairplot(df, hue='class')
print("Observations per class: \n", df['class'].value_counts())
plt.show()