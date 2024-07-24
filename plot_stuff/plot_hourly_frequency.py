import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

df = pd.read_csv('image_dates.csv')
df['Modified Date'] = pd.to_datetime(df['Modified Date'])
df['Hour'] = df['Modified Date'].dt.hour
hour_counts = df['Hour'].value_counts().reindex(range(24), fill_value=0).sort_index()

todays_date = date.today()

plt.figure(figsize=(10, 6))
plt.plot(hour_counts.index, hour_counts.values, marker='o')
plt.title('WHAT TIME OF THE DAY DO I TAKE THE PIC???? AS OF ' + str(todays_date))
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')
plt.xticks(range(24))
plt.grid(True)
plt.show()
