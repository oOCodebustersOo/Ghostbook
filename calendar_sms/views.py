from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from calendar_sms import sendSMS
from models import CalendarSMSSettings
import time
import datetime


def index(request):
	return render(request, 'calendar_sms/index.html')

def verschickt(request):
	text = request.POST['text']
	datum = request.POST['datum']
	minute = request.POST['min']
	name = request.POST['name']
	nummer = request.POST['number']
	inhalt = name + '\n' + '\n' + nummer + '\n' + text
	tag = datum.split('-')[2]
	monat = datum.split('-')[1]
	jahr = datum.split('-')[0]
	stunde = int(request.POST['hour'])
	delta = datetime.datetime(int(jahr),int(monat),int(tag),int(stunde),int(minute)) - datetime.datetime.now()
	sekunden = int(delta.total_seconds())
	ende = int(sekunden) + 600
	p = CalendarSMSSettings.objects.get(pk=1)
	p.start_time = sekunden
	p.end_time = ende
	p.save()
	print sendSMS(inhalt)
	return HttpResponseRedirect('/sms/')
