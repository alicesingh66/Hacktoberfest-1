import datetime as dt
import random
import smtplib
now = dt.datetime.now()
day = now.weekday()
file_of_quotes = ''
if day == 0:
    with open(file_of_quotes) as file:
        quotes = file.readlines()
        quote_of_day = random.choice(quotes)

    my_email = ''
    app_password = ''
    sendr_email = ''
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,to_addrs=sendr_email, msg=f'Subject:Hello\n\n{quote_of_day}')
