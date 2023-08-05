import requests
import json

#GET
user_input = input("Enter id:")
get_url =f"http://jsonplaceholder.typicode.com/todos/{user_input}"

get_response = requests.get(get_url)
print(get_response.json())

#POST

to_do_item ={"userId":2,"title":"my to do","completed":False}
post_url="http://jsonplaceholder.typicode.com/todos"

#optional header
headers = {"Content-Type":"application/json"}

#post_response =requests.post(post_url,json=to_do_item,headers=headers)
post_response =requests.post(post_url,data=json.dumps(to_do_item),headers=headers)

print(post_response.json())
