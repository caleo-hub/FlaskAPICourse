import requests

BASE = "http://127.0.0.1:5000/"

data = [ {"name": "First Video", "views": 69,"likes": 4},
         {"name": "Second Video", "views": 694,"likes": 42},
          {"name": "Third Video", "views": 6942,"likes": 422}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

response = requests.get(BASE + "video/2")
print(response.json())
response = requests.get(BASE + "video/666")
print(response.json())

response = requests.patch(BASE + "video/2", {"name": 'Funcionou'})
print(response.json())

response = requests.get(BASE + "video/2")
print(response.json())


