
import pandas as pd
import requests

# get latitude and longitude for an address
def get_lat_lng(address):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": address,
        "format": "json",
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data:
        location = data[0]
        return location['lat'], location['lon']
    else:
        return None, None

# Read the CSV file --> Pandas DataFrame
file_path = "D:/UOA WORK/Summer Research/Data_Journalism_ASRS/unique_addresses.csv" # Replace with your actual file path
df = pd.read_csv(file_path)

# Create empty columns for latitude and longitude
df['lat'] = None
df['long'] = None

# Geocode each address and fill in the latitude and longitude columns
for index, row in df.iterrows():
    address = row['address']  
    lat, lng = get_lat_lng(address)
    df.at[index, 'lat'] = lat
    df.at[index, 'long'] = lng

# Save the updated DataFrame back to the CSV file
df.to_csv("output_file.csv", index=False)  
