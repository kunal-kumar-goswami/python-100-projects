import smtplib
import datetime as dt
import pandas as pd
import random

# 🗓️ Step 1: Load birthdays from CSV
data = pd.read_csv("birthdays.csv")  # format: name,email,year,month,day
birthdays = {(row.month, row.day): row for _, row in data.iterrows()}

# 🕒 Step 2: Get today's date
today = dt.datetime.now()
today_key = (today.month, today.day)

if today_key in birthdays:
    birthday_person = birthdays[today_key]
    name = birthday_person["name"]
    email = birthday_person["email"]

    # 📝 Step 3: Pick a random letter template
    with open("letter_templates/letter_1.txt") as file:
        letters = [l.strip() for l in file.readlines() if l.strip()]
    letter = random.choice(letters)
    letter = letter.replace("[NAME]", name)

    # 📬 Step 4: Send email
    my_email = "your_email@example.com"
    password = "YOUR_PASSWORD"  # consider using environment vars

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        subject = "Happy Birthday!"
        message = f"Subject: {subject}\n\n{letter}"
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=message)
        print(f"Birthday email sent to {name} ({email})")
else:
    print("No birthdays today.")
