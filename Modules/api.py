# Function to call API
def call_api(url):
    import requests
    
    # Call API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response
    else:
        return None