import requests
import json

url = "https://api.discord.gx.games/v1/direct-fulfillment"

payload = json.dumps({
  "partnerUserId": "fdc031cf80a0ebc43f9b26d0998cdf4a148a2a6b9121f47437885434fb5b9e2e"
})
headers = {
  'authority': 'api.discord.gx.games',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'origin': 'https://www.opera.com',
  'referer': 'https://www.opera.com/',
  'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.text)

data = response.json()
print('https://discord.com/billing/partner-promotions/1180231712274387115/' + data.get('token', ''))