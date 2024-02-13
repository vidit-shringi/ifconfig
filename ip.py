# Import the requests library
import requests

# Define a function to get the IP address
def get_ip_address(number):
    # Use the ipify API to get the IP address
    url = f"https://api.ipify.org?phone={number}"
    response = requests.get(url)
    ip_address = response.text
    return ip_address

# Call the function with the number
ip = get_ip_address(number)

# Print the IP address
print(f"IP Address: {ip}")
