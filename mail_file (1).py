import smtplib
#subject import module
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#attachment import module
from email.mime.base import MIMEBase
from email import encoders

#subject starts
email_user = 'sakethreddy.kallepu@gmail.com'
email_send = 'sunnyavenger226@gmail.com'
subject = 'Python!'

# instance of MIMEMultipart 
msg = MIMEMultipart()
# storing the senders email address   
msg['From'] = email_user
# storing the receivers email address  
msg['To'] = email_send
# storing the subject  
msg['subject'] = subject
# string to store the body of the mail 
body = "hello sir,how are you?"
# attach the body with the msg instance 
msg.attach(MIMEText(body,'plain'))

# attachment starts
filename = "mail.py"   #give your filename
attachment = open(filename, 'r')
# instance of MIMEBase and named as part
part = MIMEBase("application","octet-stream")
# To change the payload into encoded form
part.set_payload((attachment).read())
# encode into base64 
encoders.encode_base64(part)
part.add_header("content-Disposition","attachment;filename = %s" %filename)
# attach the instance 'p' to instance 'msg'
msg.attach(part)
# attachment ends
text = msg.as_string()


#subject ends
server = smtplib.SMTP('smtp.gmail.com',587)
# start TLS for security
server.starttls()
# login 
server.login(email_user,'Saketh2612@')
#sending mail
server.sendmail(email_user,email_send,text)
server.close()
