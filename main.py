import random
import smtplib
import datetime as dt


MY_EMAIL = "ronel.dev@yahoo.com"
with open("password.txt") as password:
    my_password = password.read()

to_email = "kouakep.dev@gmail.com"
subject_mail = "Subject:Tuesday's weekly quote\n\n"
quote = ""
signature = "\nJe teste un code.\nRonel"

# We get the current day
now = dt.datetime.now()
today = now.weekday()

# We check if today is Tuesday
if today == 1:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
    quote = random.choice(quotes_list)

    # We send the quote in an email
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=my_password)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=subject_mail + quote + signature)
