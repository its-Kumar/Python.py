"""
Send Emails using python.

"""
import getpass
import smtplib

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.ehlo()

smtp_object.starttls()

# classic way
# password = input("what is your password? ")

# Secure way
email = getpass.getpass("Email: ")
password = getpass.getpass("Password please: ")
try:
    print(smtp_object.login(email, password))

except Exception as err:
    print(err)
    print("Log in Failed...")
    smtp_object.quit()
    exit()

from_address = email
to_address = input("Enter Address: ")
subject = input("Enter subject line: ")
message = input("Enter the body message: ")
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_address, to_address, msg)

smtp_object.quit()
