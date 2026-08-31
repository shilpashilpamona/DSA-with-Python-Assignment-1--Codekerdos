import json

response_text = """
[
  {"id":1,"name":"Ravi","email":"ravi@test.com","active":true},
  {"id":2,"name":"Priya","email":"priya@test.com","active":false},
  {"id":3,"name":"Ankit","email":"ankit@test.com","active":true}
]
"""

users = json.loads(response_text)

for user in users:
    if not user.get("active"):
        print(user["name"], "->", user["email"])
