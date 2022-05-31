import requests

endpoint = "http://localhost:8000/api/products/" # requires trailing slash here to work

get_response = requests.get(endpoint)
print(get_response.json())
