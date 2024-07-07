import json

json_string = {
  "name": "John",
  "age": 30,
  "isStudent":"True",
  "courses": ["Math", "Science", "Literature"],
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "zipcode": "10001"
  }
}
data = json.dumps(json_string)
print(data)
print(data[2:6])
print(json_string['name'])
print(json_string['courses'][1])
print(json_string["address"]["city"],json_string["address"]["zipcode"]) 