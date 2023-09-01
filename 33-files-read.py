import json 

f = open("files/test.json", "r")
# for line in f:
#     print(line)

j = json.loads(f.read())
print(j)

f.close()




