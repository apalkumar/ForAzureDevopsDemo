import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

request_paylod = {
        "userId": 125485,
        "id": 222525,
        "title": "Anil test",
        "completed": 'true'
    }

head = {
    'Content-Type' : 'application/Text',
}

head = {
    'Content-Type' : 'application/Json',
}

# Lessoon Learned : if we sent the different header type then system will respond with 500 error i.e. internal server error
response = requests.post(url=url,data=request_paylod,headers=head)
print(response.status_code)