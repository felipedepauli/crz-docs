import pandas as pd

file_name = 'data.xlsx'

df = pd.read_excel(file_name)

print(df)
print("---")


new_row = pd.DataFrame({"UNITS": [1], "TENS": [20], "HUNDREDS": [300]})

df = pd.concat([df, new_row], axis=0, ignore_index=True)

print(df)
print("---")

df['SUM'] = df['UNITS'] + df['TENS'] + df['HUNDREDS']

print(df)
print("---")

workbook = "data2.xlsx"
sheet = 'Oiew'

df.to_excel(workbook, sheet_name=sheet, index=False)