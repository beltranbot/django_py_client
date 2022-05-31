import requests

endpoint = "http://localhost:8000/api/products/3378484/" # requires trailing slash here to work

get_response = requests.get(endpoint)
print(get_response.json())
