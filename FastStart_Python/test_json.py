

import json

with open('example.json') as f:
    data = json.loads(f.read())
print(data)
print(type(data))

del data['String']

data["numberKey"] = 100

print(data)

with open('out.json', 'w+') as f:
    f.write(json.dumps(data))
