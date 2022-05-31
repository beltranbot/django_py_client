import requests

product_id = input("What is the product id you want to use?\n")

try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid id')

if product_id:


    # requires trailing slash here to work
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/" 

    delete_response = requests.delete(endpoint)
    print(delete_response.status_code)
