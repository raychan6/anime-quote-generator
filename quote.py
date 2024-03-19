import requests

response = requests.get("https://animechan.xyz/api/random")

if response.status_code == 200:
    print(response.json()['quote'] + ' -' + response.json()['character'] + ' (' + response.json()['anime'] + ')')
else:
    print("Unable to connect to the server. Please try again later.")