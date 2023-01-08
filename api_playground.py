# 1. Import necessary libraries
import requests

# 2. Make request
url = "http://fakestoreapi.com/carts/user/2"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
response.raise_for_status #returns HTTPError object if error occurs
print(response.text)

# 3. Save to file
# with open("api_playground_response.txt", "w") as f:
#     f.write(response.text)
