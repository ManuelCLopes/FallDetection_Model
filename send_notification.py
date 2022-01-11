from email import message
import smtplib

import email.utils
from email.mime.text import MIMEText

def send_email():
   EMAIL_SENDER = "falldetection.isi@gmail.com"
   PASSWORD = "%GB675R87t87bn7Ss_Ss"

   sender = EMAIL_SENDER
   receivers = ['manuelclopes99@gmail.com']


   # Create the message
   msg = MIMEText('It was detected a fall of  worker xxxxx on location yyyyy.')
   msg['To'] = email.utils.formataddr(('Manager1',
                                       receivers[0]))
   msg['From'] = email.utils.formataddr(('Fall Detection System',
                                       EMAIL_SENDER))
   msg['Subject'] = 'FALL ALERT!'

   smtpObj = smtplib.SMTP('smtp.gmail.com')
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(EMAIL_SENDER, PASSWORD)

   smtpObj.set_debuglevel(True)
   try:
      smtpObj.sendmail(sender, receivers, msg.as_string())         
      return True
   except:
      return False