# Import the required libraries
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import folium

# Define the phone number to track
number = input("Enter the number with country code [+919876543210]") # Change this to the number you want to track

# Parse the phone number
parsed_number = phonenumbers.parse(number)

# Get the country name
country = geocoder.description_for_number(parsed_number, "en")

# Get the carrier name
carrier_name = carrier.name_for_number(parsed_number, "en")

# Get the time zone
time_zone = timezone.time_zones_for_number(parsed_number)

# Print the information
print(f"Country: {country}")
print(f"Carrier: {carrier_name}")
print(f"Time zone: {time_zone}")

# Use OpenCage Geocoding API to get the coordinates of the country
# You need to get an API key from https://opencagedata.com/
api_key = "YOUR_API_KEY" # Replace this with your API key
base_url = "https://api.opencagedata.com/geocode/v1/json"
params = {"q": country, "key": api_key}
response = requests.get(base_url, params=params)
data = response.json()

# Get the latitude and longitude
lat = data["results"][0]["geometry"]["lat"]
lng = data["results"][0]["geometry"]["lng"]

# Create a map using folium
map = folium.Map(location=[lat, lng], zoom_start=5)
folium.Marker([lat, lng], popup=country).add_to(map)

# Save the map as an html file
map.save("map.html")
