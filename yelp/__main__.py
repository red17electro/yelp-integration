import requests

url = "https://api.yelp.com/v3/events"

payload = {}
headers = {
  'Authorization': 'Bearer EST24WiV5UEu-BGZFd7vKtHGcAUa7-rn4Pl0N_a9SVBqvOpYmlezH44rtYxtZQ7oDl6KtA2uNuBqlfha_WJKRsbwElJI_-iWZIXDo01KERC1rJ_nksJecLYch6TjXnYx'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
