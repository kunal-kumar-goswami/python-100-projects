import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 172
AGE = 21

APP_ID = "9918a10c"
API_KEY = "d83d39900643b4fc6488044f63da207e"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/c96ff2700f73b070634fb5ba32d62aca/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint, 
  json=sheet_inputs, 
  auth=(
      "kunal ", 
      "Abc123@&99.",
  )
)

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer a3VuYWwgOkFiYzEyM0AmOTku"
}
sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)
print(f"Sheety Response: \n {sheet_response.text}")
