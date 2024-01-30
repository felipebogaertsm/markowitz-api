import requests
import json

# Define the API endpoint
URL = "http://localhost:8000/api/optimizer"  # Update with the correct URL

# Define the data to be sent to the API
data = {
    "tickers": "AAPL,MSFT,GOOGL",
    "from_date": "2022-01-01",
    "to_date": "2023-12-31",
    "target_return": 0.1,
}

# Make the POST request
response = requests.post(
    URL, data=json.dumps(data), headers={"Content-Type": "application/json"}
)

# Print the response
if response.status_code == 200:
    print("Success!")
    print("Response data:", response.json())
else:
    print("Failed to get a response.")
    print("Status code:", response.status_code)
    print("Response data:", response.text)
