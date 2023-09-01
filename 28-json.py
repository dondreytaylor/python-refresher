import json 

x = '{"name": "Dondrey Taylor"}'
y = json.loads(x)
print(y["name"])

x = {
  "name": "Dondrey Taylor",
  "age": 31,
  "city": "New Jersey"
}
y = json.dumps(x)
print(y)