import smtplib
import datetime as dt
import random

MY_EMAIL = "YOUR_MAIL"
MY_PASS = "YOUR_PASSWORD "

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="RECEIVER_MAIL", msg=f"Subject: Monday Motivation\n\n Here is a dose of motivation for the week:-\n {quote}")
