import smtplib, ssl
def sendAlertEmail(confidence):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com" # sampe server
    sender_email = "my@gmail.com"  # sample sender address
    receiver_email = "your@gmail.com"  # sample receiver address
    password = "password" # sample password
    message = "Intruder has been detected with ${confidence} confidence"
    # send email with server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def sendErrorEmail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com" # sampe server
    sender_email = "my@gmail.com"  # sample sender address
    receiver_email = "your@gmail.com"  # sample receiver address
    password = "password" # sample password
    message = "Detected error with camera"
    # send email with server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)