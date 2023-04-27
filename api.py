import requests
import json

# Запрос GET

status = 'available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                    headers = {'accept': 'application/json'})
res_status = res.status_code
try:
    result = res.json()
except:
    result = res.text

print(result)
print(res_status)

# Запрос POST
body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

res = requests.post("https://petstore.swagger.io/v2/pet",
                    headers=headers,
                    data=json.dumps(body, ensure_ascii=False))

res_status = res.status_code
result1 = ' '
try:
    result1 = res.json()
except:
    result1 = res.text

print(result1)
print(res_status)

# Запрос Delete
pet_id = result1['id']
res = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
res_status = res.status_code
result = ''
try:
    result = res.json()
except:
    result = res.text

print(result)
print(res_status)

# Запрос Put

new_body = ({
  "id": 0,
  "category": {
    "id": 0,
    "name": "drakon"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

res = requests.put("https://petstore.swagger.io/v2/pet", headers=headers, data=json.dumps(new_body, ensure_ascii=False))
res_status = res.status_code
result = ''
try:
    result = res.json()
except:
    result = res.text
print(result)
print(res_status)
