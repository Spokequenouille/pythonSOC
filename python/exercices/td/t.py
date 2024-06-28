import smtplib
from email.mime.text import MIMEText


sender = 'spkqnll@gmail.com'

receivers = ['antoine.schulz@outlook.fr']
password = "xhyd nyne sixy zcpb"
subject = "Email Subject"
body = "This is the body of the text message"

def send_email(subject, body, sender, receivers, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(receivers)
    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(sender, password)
    message = body
    s.sendmail(sender,receivers,message)
    s.quit()
    print("Message sent!")


send_email(subject, body, sender, receivers, password)