# Import the requests library
import requests

# Define the IP address you want to query
ip = "8.8.8.8"

# Define the API key for IPinfo (you can get a free one from their website)
api_key = "YOUR_API_KEY"

# Define the URL for the IPinfo API
url = f"https://ipinfo.io/{ip}?token={api_key}"

# Make a GET request to the URL and get the response
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response as JSON
    data = response.json()

    # Print the device information
    print(f"Device type: {data['device']['type']}")
    print(f"Device model: {data['device']['model']}")
    print(f"Operating system: {data['os']['name']} {data['os']['version']}")
    print(f"Browser: {data['browser']['name']} {data['browser']['version']}")
else:
    # Print an error message
    print(f"Error: {response.status_code}")
