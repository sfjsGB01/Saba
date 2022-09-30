import json
import requests

BASE_URL='https://fakestoreapi.com'

all_products_response=requests.get(f"{BASE_URL}/products")
print(all_products_response.json())

for product in all_products_response.json():
    print(f"{product['title']} costs ${product['price']}")

products_5_response=requests.get(f"{BASE_URL}/products/10")
print(products_5_response.json())

query_params={"limit":4}
products_limit_response=requests.get(f"{BASE_URL}/products",params=query_params)
print(products_limit_response.json())

query_params={"sort":"desc"}
products_sort_response=requests.get(f"{BASE_URL}/products",params=query_params)
print(products_sort_response.json())

products_category_response=requests.get(f"{BASE_URL}/products/categories")
print(products_category_response.json())

new_product = {
                    "title": 'test product-new',
                    "price": 13.5,
                    "description": 'lorem ipsum set',
                    "image": 'https://i.pravatar.cc',
                    "category": 'electronic'
                }

response=requests.post(f"{BASE_URL}/products",json=new_product)
print(response.json())

headers={
    "Content-Type":"application/json"
}
response=requests.post(f"{BASE_URL}/products",data=json.dumps(new_product),headers=headers)
print(response.json())

update_prod = {
    "title": 'test product- x',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response=requests.put(f"{BASE_URL}/products/1",json=update_prod)
print(response.json())

res=requests.delete(f"{BASE_URL}/products/11")
print(res.json())




