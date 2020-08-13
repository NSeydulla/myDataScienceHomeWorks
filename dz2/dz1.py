import pandas as pd
data = pd.read_csv('teams_stats.csv', delimiter=',')
print(len(data['Tm'].value_counts()))
