import requests
from datetime import datetime

USERNAME = "kunal123" 
TOKEN = "jhyfyrshjty5w45trfkhfj563e5ytfc"
GRAPH_ID = "graph4"


pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,  
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("How many kilometers did you cyclr today? "),

}

response = requests.post(url = pixel_creation_endpoint, json= pixel_data,headers= headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint,json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}>" 

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)