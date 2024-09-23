from dotenv import dotenv_values

# Load secrets
my_secrets = dotenv_values(".env")

# Import ngrok python sdk
import ngrok
import time

# Establish connectivity
listener = ngrok.forward(5000, authtoken=my_secrets["NGROK_ACCESS_TOKEN"])

# Output ngrok url to console
print(f"Ingress established at {listener.url()}")

# Keep the listener alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing listener")