#!/bin/bash
# install.sh

# Install the required libraries using pip
pip install phonenumbers requests folium

# Install the OpenCage Geocoding API key
# You need to get an API key from https://opencagedata.com/
# and replace YOUR_API_KEY with your actual key
echo "export OPENCAGE_API_KEY=YOUR_API_KEY" >> ~/.bashrc
source ~/.bashrc

# Run the python code
python phone.py
