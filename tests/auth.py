import requests

client_id = "AUv8rrc_P-EbP2E0mpb49BV7rFt3Usr-vdUZO8VGOnjRehGHBXkSzchr37SYF2GNdQFYSp72jh5QUhzG"
client_secret = "EMnAWe06ioGtouJs7gLYT9chK9-2jJ--7MKRXpI8FesmY_2Kp-d_7aCqff7M9moEJBvuXoBO4clKtY0v"

payloads = {
    "grant_type": "client_credentials",
    "ignorecache": "true",
    "return_auth_schemas": "true",
    "return_client_metadata": "true",
    "return_unconsented_scopes": "true"
}

response = requests.post(
    url="https://api-m.sandbox.paypal.com/v1/oauth2/token",
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    auth=(client_id, client_secret),
    data=payloads
)

print(response.json())

print(response.json()["access_token"])


