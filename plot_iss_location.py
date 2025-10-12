import pandas as pd
import matplotlib.pyplot as plt
import json

# Read the ISS location data
data = []
with open('iss-location.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line))

# Create a DataFrame
df = pd.DataFrame(data)
df['latitude'] = df['iss_position'].apply(lambda x: float(x['latitude']))
df['longitude'] = df['iss_position'].apply(lambda x: float(x['longitude']))

# Plot the data
plt.figure(figsize=(10, 5))
img = plt.imread("equirectangular-projection-world-map.jpg")
plt.imshow(img, extent=[-180, 180, -90, 90])
plt.scatter(df['longitude'], df['latitude'], s=1, color='red')
plt.title('ISS Location')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('iss_location.png')
