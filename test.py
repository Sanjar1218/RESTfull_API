import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":1012, "name":"T1adim", "views":1000},
        {"likes":10, "name":"dont make mistake", "views":1},
        {"likes":11231012, "name":"gfadsf", "views":10234200}
]

for i in range(len(data)):
    response = requests.put(BASE + "/video/"+str(i),data[i])
    print(response.json())

input()
response = requests.delete(BASE + "/video/0")
print(response)
input()

response = requests.get(BASE + "/video/2")
print(response.json())
