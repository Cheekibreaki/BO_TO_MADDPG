import json

# File path
file_path = './base_map4_config1_cache.json'

# Read data from file
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert the value to float for comparison
for item in data:
    item['value'] = float(item['value'])

# Find the max and min values
max_value = max(data, key=lambda x: x['value'])
min_value = min(data, key=lambda x: x['value'])

print(f"Maximum Value: {max_value['value']}")
print(f"Minimum Value: {min_value['value']}")


def inverse_value(data):
    # Convert the value to float for calculation
    for item in data:
        item['value'] = float(item['value'])

    # Find the max value to scale the inverse values
    max_value = max(data, key=lambda x: x['value'])['value']

    # Calculate inverse values scaled by the max value
    for item in data:
        # Inverse value calculation (scaled by max value)
        item['inverse_value'] = 1 - (item['value'] / max_value)

    return data


# Apply the function
result = inverse_value(data)

# Overwrite the file with the new data
with open(file_path, 'w') as file:
    json.dump(result, file, indent=4)

print("File overwritten with new data.")