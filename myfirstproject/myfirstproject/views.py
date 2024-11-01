from django.shortcuts import render
# 7 - import libraries for email sending
from django.http import HttpResponse
from django.core.mail import send_mail
from . import settings

def index(request):

    # 8 - sending the mail
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['laraibe@gmail.com','axel_senechal@hotmail.com','Yanis5005@gmail.com'],
                  fail_silently=False
                  )
    return render(request, 'index.html')  # Ensure index.html is in the correct location
