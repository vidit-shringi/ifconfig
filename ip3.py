import requests

def get_ip_info(ip):
    # make a GET request to the ipapi API with the IP address
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    # check if the response status code is 200 (OK)
    if response.status_code == 200:
        # parse the JSON response into a dictionary
        data = response.json()
        # return the data dictionary
        return data
    else:
        # raise an exception if the response status code is not 200
        raise Exception(f'Error: {response.status_code}')

# test the function with an example IP address
ip = input("Enter IP address here:")
info = get_ip_info(ip)
print(info)
