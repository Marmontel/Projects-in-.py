from email import message
import simplejson
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
message = 'Write your message here'

# Credentials and email subject

password = 'Password your e-mail'
msg['From'] = 'Sender e-mail'
msg['To'] = 'Recipient email'
msg['Subject'] = 'Subject your e-mail'

# Set up the connection and send email

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
