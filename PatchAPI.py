import requests
import json

url = "https://jsonplaceholder.typicode.com/todos/12544378"

response = requests.patch(url=url)

print(response.status_code)