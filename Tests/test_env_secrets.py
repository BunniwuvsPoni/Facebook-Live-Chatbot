from dotenv import dotenv_values

# Load secrets
my_secrets = dotenv_values(".env")

# Print all secrets from .env file
print(my_secrets)

# Print a dedicated secret
print(my_secrets["FACEBOOK_PAGE_ACCESS_TOKEN"])