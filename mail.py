import smtplib     #secure mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = "sakethreddy.kallepu@gmail.com"  #give your email id
email_send = "girikumar.kolla@gmail.com"   #give receiver id

subject = "Python"
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = 'Python'
body = "Hello! first mail using python script" # The /n separates the message
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login(email_user, "Saketh2612@")
#Send the mail
server.sendmail(email_user, email_send, text) 
server.quit()
