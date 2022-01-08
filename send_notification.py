import smtplib

EMAIL_SENDER = "falldetection.isi@gmail.com"
PASSWORD = "%GB675R87t87bn7Ss_Ss"

sender = EMAIL_SENDER
receivers = ['manuelclopes99@gmail.com', 'pv22382@alunos.estgv.ipv.pt']

message = """From: Fall Alert! <falldetection.isi@gmail.com>
To: Manager <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""


smtpObj = smtplib.SMTP('smtp.gmail.com')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(EMAIL_SENDER, PASSWORD)

smtpObj.set_debuglevel(True)
try:
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except:
   print ("Error: unable to send email")



