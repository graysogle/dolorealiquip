import pandas as pd
import json

# Sample JSON data
json_data = '''
{
  "id": 1,
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  },
  "email": [
    "john@example.com",
    "john@gmail.com"
  ]
}
'''

# Load JSON data into a dictionary
data = json.loads(json_data)

# Normalize the JSON data into a dataframe
df = pd.json_normalize(data)

# Print the dataframe
print(df)
