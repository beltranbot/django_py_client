import requests

endpoint = "http://localhost:8000/api/products/1/update/" # requires trailing slash here to work

# data that I want to updaet
data = {
    "title": "Hello world",
    "price": 00.00
}

put_response = requests.put(endpoint, json=data)
print(put_response.json())
