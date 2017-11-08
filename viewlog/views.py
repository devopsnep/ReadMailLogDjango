from django.shortcuts import render
from django.http import HttpResponse
import os
def readLog(request):
    command = 'tail -n 100 /var/log/mail.log'
    output = os.popen(command).readlines()
    return render(request,'log.html',{'output':output})

def index(request):
    return HttpResponse('<p>django: site is unavailable</p>')