# Enables the importing of modules
import import_modules
import_modules.activate_import_modules()

# Test starts here:
import api_utilities

# Test API call
test_url = "https://graph.facebook.com/facebook/picture?redirect=false"
test_response = api_utilities.call_api(test_url)
print(test_response.status_code)
print(test_response.text)