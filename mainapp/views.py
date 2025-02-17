from django.shortcuts import render, HttpResponse
from .tasks import task_func
from send_mail_app.tasks import send_mail_func

def test(request):
    task_func.delay()
    return HttpResponse("Done")

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")