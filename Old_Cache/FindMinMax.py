import json

# File path
file_path = 'E:/Summer Research 2023/BO_to_MADDPG/BO_TO_MADDPG/Old_Cache/base_map3_config1_cache.json'

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
        item['inverse_value'] = max_value / item['value']

    return data


# Apply the function
result = inverse_value(data)

# Print the results
for item in result:
    print(f"Original step Value: {item['value']}, Inverse Value: {item['inverse_value']}")