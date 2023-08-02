import requests
import json

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url=url)
print("Response Status Code is --->",response.status_code)
file1 = response.text
file3 = json.loads(file1)
print(type(file3))
# Dictionary Count in List Using filter() and lambda function
# res = len(list(filter(lambda x: isinstance(x, dict), file3)))
# printing result
# print("The Dictionary count : " + str(res))

# Dictionary Count in List, # Using sum method
res = sum(1 for i in file3 if type(i) == dict)
# printing result
print("The Dictionary count : " + str(res))

# print(len(file3[2]))
# print(type(file3[__dict__]))
# print(file3[1]["userId"])
# print(file3[1]["id"])
# print(file3[1]["title"])
# print(file3[1]["completed"])
# print(file3)
# file1 = response.json()
# file2 = json.dumps(file1, indent=4)
# print(file2)
# print(type(file2))
# file3
# print(response.text.count("quis ut nam facilis et officia qui"))

