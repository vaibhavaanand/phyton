import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login("*****8*@gmail.com", "password")

message  = "test email"

s.sendmail("*************@gmail.com","************@gmail.com", message)
print("successful")
s.quit()