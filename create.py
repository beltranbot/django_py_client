import requests

endpoint = "http://localhost:8000/api/products/" # requires trailing slash here to work

data = {
    "title": "This field is done",
    "price": 32.99
}
post_response = requests.post(endpoint, json=data)
print(post_response.json())
