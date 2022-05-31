import requests


endpoint = "https://httpbin.org"
endpoint = "https://httpbin.org/anything"  # echoes back what is send
endpoint = "https://httpbin.org/anything"  # echoes back what is send
endpoint = "http://localhost:8000/api/" # requires trailing slash here to work

# get_response = requests.get(endpoint, json={
#     "query": "hello world"
# })
# print(get_response.json())

# GET request
get_response = requests.get(
    endpoint,
    params={"abc": 123},
    json={"query": "Hello world"}
)

# next 2 lines for work for a json response
print(get_response.json())
print(get_response.status_code)

# next lines are for httpResponse
# print(get_response.headers)
# print(get_response.text)


# POST request
# post_request = requests.post(
#     endpoint + "post/",
#     json={"title": "This is a title", "price": 12.69}
# )

# print(post_request)
# print(post_request.json())
# print(post_request.status_code)
