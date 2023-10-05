from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings

EMAIL = "alexandreanpita@gmail.com"

def sendEmail():
    TITLE = "Obrigado por teres aceitado!! <3"
    HTML_MESSAGE = render_to_string('email2.html', {})
    MESSAGE = strip_tags(HTML_MESSAGE)
    #print(MESSAGE, EMAIL)
    return (send_mail(
        TITLE,
        MESSAGE,
        settings.EMAIL_HOST_USER,
        [EMAIL],
        fail_silently=False,
        html_message=HTML_MESSAGE
    ))