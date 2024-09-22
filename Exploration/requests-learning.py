import requests

# Function to call API
def call_api(url):
    # Call API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response
    else:
        return None


# Test API call
test_url = "https://api.github.com/events"
test_response = call_api(test_url)
print(test_response.status_code)
print(test_response.text)