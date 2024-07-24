import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date

df = pd.read_csv('image_dates.csv')
df['Modified Date'] = pd.to_datetime(df['Modified Date'])

df['Year'] = df['Modified Date'].dt.year
df['Hour'] = df['Modified Date'].dt.hour
df['Minute'] = df['Modified Date'].dt.minute

df['Time of Day (Minutes)'] = df['Hour'] * 60 + df['Minute']

average_time_per_year = df.groupby('Year').agg({
    'Time of Day (Minutes)': 'mean',
    'Year': 'count'
}).rename(columns={'Year': 'File Count'}).reset_index()

todays_date = date.today()

average_time_per_year['Average Hour'] = average_time_per_year['Time of Day (Minutes)'] // 60
average_time_per_year['Average Minute'] = average_time_per_year['Time of Day (Minutes)'] % 60
average_time_per_year['Average Time'] = average_time_per_year['Average Hour'].astype(int).astype(str).str.zfill(2) + ':' + average_time_per_year['Average Minute'].astype(int).astype(str).str.zfill(2)



plt.figure(figsize=(12, 7))
plt.plot(average_time_per_year['Year'], average_time_per_year['Time of Day (Minutes)'], marker='o', linestyle='-')
plt.title('Average Time of Day for Each Year AS OF ' + str(todays_date))
plt.xlabel('Year')
plt.ylabel('Average Time of Day (Minutes)')
plt.grid(True)
plt.xticks(average_time_per_year['Year'])
plt.yticks(np.arange(0, 1440, step=60), [f'{hour:02d}:00' for hour in range(24)])

plt.show()