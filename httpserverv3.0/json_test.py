import json

js = json.dumps({'a':1,'b':'hello'})

print(type(js))

js = json.loads(js)
print(js)
print(type(js))