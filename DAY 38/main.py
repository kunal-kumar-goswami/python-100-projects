import requests
from datetime import datetime

# Constants
GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 172
AGE = 21

APP_ID = "YOUR API ID"
API_KEY = "YOUR API KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/c96ff2700f73b070634fb5ba32d62aca/copyOfMyWorkouts/workouts"

# Input exercise text from the user
exercise_text = input("Tell me which exercises you did: ")

# Set up headers for the request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Set up parameters for the exercise API request
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send the request to the exercise API
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Get the current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Loop through the exercises in the response and add them to the Google Sheets
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

    # Send data to Google Sheets with Basic Authentication
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=("kunal", "Abc123@&99.")  # Basic Auth credentials
    )

    # Print response for each workout
    print(f"Sheety Response: \n {sheet_response.text}")
