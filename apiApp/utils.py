from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_email(data):
        
        print(data)
        # Reading html page 
        with open('apiApp/mailHtml.html','r') as file:
            html_content = file.read()

        email = EmailMessage(
            subject="Hurrah ! You got a new Client.",
            body=data["name"]+data["cName"]+data["email"]+data["additionalDetails"],
            to=["ptcsam74@gmail.com"]
        )

        email.content_subtype = 'html'
        email.body = html_content.replace('idname',data["name"])
        # email.body = html_content.replace('idcompany',data["cName"])
        # email.body = html_content.replace('idemail',data["email"])
        # email.body = html_content.replace('idmessage',data["additionalDetails"])

        print(email.body)
        email.send()

from django.core.mail import send_mail
from django.conf import settings 

def send_mail_to(data):
    subject = "Subject of the mail"
    message = "Message of the email"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ptcsam74@gmail.com "]

    send_mail(subject, message, from_email, recipient_list)