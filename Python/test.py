import requests

def make_api_request():
    api_url = 'https://catfact.ninja/facts?limit=1&max_length=140'

    # Make a GET request using the requests library
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Handle the data here
        print('API Response:', data)
    else:
        # Handle the error
        print('Error:', response.status_code, response.text)

# Call the function to make the API request
make_api_request()
