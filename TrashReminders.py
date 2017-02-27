import smtplib
import datetime
import os

#Function to
def load_configurationData():
    recipientLocation = os.getcwd() + "\Recipients.txt"
    with open(recipientLocation) as f:
        recipients = f.read().splitlines()

    return recipients

def sendEmail(email, pw, recipient, message):
    # Setup email server and send the message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, pw)
    server.sendmail(email, recipient, message)
    server.close()

# Get the recepients, email and pw from config file
recipients = load_configurationData()
emailSender = recipients.pop()
password = recipients.pop()

#default messages
takeOutTrash = "Its your turn to take out the trash"
bringBinsInside = "Dont forget to bring the bins back in"


sendEmail(emailSender, password, recipients.pop(), takeOutTrash)
