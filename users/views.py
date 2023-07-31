from django.shortcuts import render, redirect

from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse


from django.core.mail import send_mail

from pytodo import settings
import smtplib
import ssl



class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    
    def form_valid(self, form: UserCreationForm):
        user = form.save()
        login(self.request, user)
        return redirect("/")


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm


# class CustomLogoutView(LogoutView):
#     template_name = 


# def user_exit(request):
#     logout(request)
#     return redirect("/")


# class SendEmail(View):
#     def get(self, request):
#         message = "Hello, world!"
#         # post_server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
#         # post_server.ehlo()
#         # post_server.starttls(context=ssl.create_default_context())
#         # post_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#         # post_server.sendmail(settings.EMAIL_HOST_USER, "example@gmail.com", message)
#         # post_server.quit()
#         send_mail("Mail to example@gmail.com",message,settings.EMAIL_HOST_USER,
#         ['example@gmail.com'])

#         return HttpResponse('Mesage sent')


    
    
# class SendMessageView(View):
#     def get(self, request):
#         message = "Hello, world!"
#         post_server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
#         post_server.ehlo()
#         post_server.starttls(context=ssl.create_default_context())
#         post_server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#         post_server.sendmail(settings.EMAIL_HOST_USER, "yaku19760@gmail.com", message)
#         post_server.quit()
        
#         return HttpResponse("Повідомлення відправлено")
