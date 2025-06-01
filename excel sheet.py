import pandas as pd


df = pd.read_excel('input.xlsx')


df['Total'] = df.iloc[:, 1:].sum(axis=1)
df['Percentage'] = df['Total'] / (df.shape[1] - 2) 


def grade(pct):
    if pct >= 90:
        return 'A+'
    elif pct >= 80:
        return 'A'
    elif pct >= 70:
        return 'B'
    elif pct >= 60:
        return 'C'
    else:
        return 'F'

df['Grade'] = df['Percentage'].apply(lambda x: grade(x * 100))


df.to_excel('output.xlsx', index=False)
print("Marksheet generated and saved as output.xlsx")
