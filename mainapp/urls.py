from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.test, name="test"),
    path("send_mails/", views.send_mail_to_all, name="sendmails"),

]
