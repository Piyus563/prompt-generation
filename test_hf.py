import requests
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
output = query({
    "inputs": "Write a highly detailed prompt for an AI assistant to act as a prompt engineer for the idea: I want to start a food blog",
})
print(output)
