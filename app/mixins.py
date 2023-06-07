import smtplib
import ssl
from email.message import EmailMessage
import random
otp = random.randrange(1111,9999)
tmp = str(otp)

for i in range(1,2):
    email_sender = 'dhrumilparekh1273@gmail.com'
    
    email_password = 'spoldfcfzqqoevus'
    email_receiver = "jayrajsinhvaghela1108@gmail.com"
    subject = "OTP"
    body = """
    Welcome to Astha Clinic
    Your OTP is : """ + tmp  #.format(otp)
    em = EmailMessage()
    em['from'] = email_sender
    em['to'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
        print("done")