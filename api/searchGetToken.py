# simple script to get a token
# searches for 'token' in the response
# 

import requests

# URL of the API endpoint to get the token
url = 'http://192.168.56.101/v3/'  # Your specified endpoint

# JSON body for the POST request to get the token
payload = {
    "name": "login",
    "param": {
        "user": "securestore",  # Replace if necessary
        "pass": "securestore"   # Replace if necessary
    }
}

# Headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Function to recursively search for a key in a nested dictionary and track its location
def find_token(data, key='token', path=''):
    if isinstance(data, dict):
        # If it's a dictionary, check each key-value pair
        for sub_key, sub_value in data.items():
            new_path = f"{path}.{sub_key}" if path else sub_key  # Construct the path
            if sub_key == key:
                return sub_value, new_path  # Return the token and its path
            result, result_path = find_token(sub_value, key, new_path)  # Recur for nested dict
            if result:
                return result, result_path
    elif isinstance(data, list):
        # If it's a list, iterate over the elements
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"  # Path for list elements
            result, result_path = find_token(item, key, new_path)
            if result:
                return result, result_path
    return None, None

# Send the POST request to retrieve the token
response = requests.post(url, json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()

    # Search for the token and its location in the entire response
    token, token_path = find_token(response_data, key='token')

    if token:
        print(f"Token: {token}")
        print(f"Token found at: {token_path}")
    else:
        print("Token not found in the response.")
        print(f"Response data: {response_data}")  # Print the full response for debugging
else:
    print(f"Failed to get token. Status code: {response.status_code}, Response: {response.text}")
