import requests
endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": "https://bit.ly/3yxKEIY"
}
headers = {
    "authorization": "1384ecc6060243c68dadf06bdcbdaf0f",
    "content-type": "application/json"
}
response = requests.post(endpoint, json=json, headers=headers)
print(response.json())
