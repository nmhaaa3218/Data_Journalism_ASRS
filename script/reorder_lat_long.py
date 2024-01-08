# Import library
import pandas as pd

# Read the data
df = pd.read_csv('output_file.csv')

# Reorder the columns
df = df[["address","long", "lat"]]

# Save the data
df.to_csv('wa_unique_coords.csv', index=False)