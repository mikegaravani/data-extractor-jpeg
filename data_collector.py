import os
from datetime import datetime
import pandas as pd

def get_modified_date(file_path):
    try:
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"Error getting modified date for {file_path}: {e}")
        return None

def collect_image_dates(directory):
    image_dates = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                file_path = os.path.join(root, file)
                modified_date = get_modified_date(file_path)
                if modified_date:
                    image_dates.append((file, modified_date))
                else:
                    print(f"No modified date found for {file}")
    return image_dates

if __name__ == "__main__":
    directory = input("Enter the directory path containing JPEG images: ")
    image_dates = collect_image_dates(directory)
    
    image_dates.sort(key=lambda x: datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S'))
    df = pd.DataFrame(image_dates, columns=['File Name', 'Modified Date'])
    output_file = 'image_dates.csv'
    df.to_csv(output_file, index=False)
    
    print(f"Data has been written to {output_file}")
