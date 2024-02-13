# Import the requests library
import requests

# Define the phone number you want to query
phone = "+919876543210"

# Define the API key for NumVerify (you can get a free one from their website)
api_key = "YOUR_API_KEY"

# Define the URL for the NumVerify API
url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone}"

# Make a GET request to the URL and get the response
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Print the device information
    print(f"Country: {data['country_name']}")
    print(f"Carrier: {data['carrier']}")
    print(f"Line type: {data['line_type']}")
else:
    # Print an error message
    print(f"Error: {response.status_code}")
