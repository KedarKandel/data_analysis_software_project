import requests
import json

# zoo dataset api
url = 'https://korkeasaarenkavijat.onrender.com/api/data/year'

try:
    # Send GET request
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes

    # Parse JSON response
    data = response.json()

    # Save to data.json
    with open('data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Data saved to data.json successfully!")

except requests.RequestException as e:
    print(f"An error occurred while fetching data: {e}")
except ValueError as ve:
    print(f"Error parsing JSON: {ve}")
