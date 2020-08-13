import pandas as pd
data = pd.read_csv('Mountains.csv', delimiter=',')
s = data['Parentmountain'].value_counts()
for i in range(len(s)):
    if s[i] == 3:
        s = s[:i]
        break
print(s)
