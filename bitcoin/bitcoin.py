import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# Replace with your actual CoinCap v3 API key
api_key = "YOUR_API_KEY_HERE"

try:
    response = requests.get(
        "https://api.coincap.io/v3/assets/bitcoin",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = bitcoins * price
    print(f"${total:,.4f}")
except requests.RequestException:
    sys.exit("Error fetching data")
