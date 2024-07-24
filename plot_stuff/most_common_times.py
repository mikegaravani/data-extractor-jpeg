import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

df = pd.read_csv('image_dates.csv')
df['Modified Date'] = pd.to_datetime(df['Modified Date'])
df['Hour:Minute'] = df['Modified Date'].dt.strftime('%H:%M')
time_counts = df['Hour:Minute'].value_counts()
time_counts_df = time_counts.reset_index()
time_counts_df.columns = ['Hour:Minute', 'Count']

top_n = 12
top_times = time_counts_df.head(top_n)

todays_date = date.today()

plt.figure(figsize=(10, 7))
plt.barh(top_times['Hour:Minute'][::-1], top_times['Count'][::-1], color='skyblue')
plt.title('Top {} Most Common Hour:Minute Combinations AS OF '.format(top_n) + str(todays_date))
plt.xlabel('Frequency')
plt.ylabel('Hour:Minute')
plt.grid(axis='x')
max_count = top_times['Count'].max()
plt.xticks(np.arange(0, max_count + 1, step=1))
plt.show()