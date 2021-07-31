import requests

BASE = "http://127.0.0.1:5000/"

print("First time requesting for search keyword 'a' ")
response = requests.get(BASE + "find/freq/a")
print(response.json())
print("Second time requesting for search keyword 'a' ")
response = requests.get(BASE + "find/freq/a")
print(response.json())
print("First time requesting for search keyword 'hello' ")
response = requests.get(BASE + "find/freq/hello")
print(response.json())
print("First time requesting for search keyword 'bye' ")
response = requests.get(BASE + "find/freq/bye")
print(response.json())
print("Second time requesting for search keyword 'hello' ")
response = requests.get(BASE + "find/freq/hello")
print(response.json())
print("Third time requesting for search keyword 'a' ")
response = requests.get(BASE + "find/freq/a")
print(response.json())

