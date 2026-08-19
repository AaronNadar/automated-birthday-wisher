import os
import pandas
import datetime as dt
import random
import smtplib

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:

    with open(fr"letter_templates\letter_{random.randint(1,3)}.txt") as txt:
        text = txt.read()
        wish = text.replace("[NAME]", birthday_dict[today]['name']).strip()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_dict[today]['email'],
                            msg=f"Subject: Happy Birthday!\n\n "
                                f"{wish}")
