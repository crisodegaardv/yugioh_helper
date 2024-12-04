import requests

response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Sky+Striker+Ace+-+Raye")
card_data = response.json()

print(card_data["data"][0]["desc"])