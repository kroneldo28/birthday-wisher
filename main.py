import smtplib


my_email = "ronel.dev@yahoo.com"
with open("password.txt") as password:
    my_password = password.read()

with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="kouakep.dev@gmail.com", msg="Subject:Test\n\nThis is a test mail")

