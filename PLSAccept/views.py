from django.shortcuts import render
from django.conf import settings
from . import email
# Create your views here.
def index(request, token):
   
    if(token!=settings.TOKEN):
        raise Exception("Wrong Token")
    try:
        print(settings.STATICFILES_DIRS, settings.STATIC_ROOT)
    except Exception as e:
        print(e.with_traceback)
    return render(request,"index.html",{"token":token})

def accept(request, token):
    if(token!=settings.TOKEN):
        raise Exception("Wrong Token")
    email.sendEmail()
    return render(request, "accept.html",{})