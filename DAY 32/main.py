import smtplib
import datetime as dt 
import random 

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0 :
    with open("/python/100 Days of Code/DAY 32/quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smpt.gmail.com") as connection :
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivaion\n\n{quote}")


