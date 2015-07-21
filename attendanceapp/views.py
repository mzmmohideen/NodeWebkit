from attendanceapp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
import json,os
from django.http import HttpResponse
from django.shortcuts import render

def login(request):
	return render(request, 'login.html')

@csrf_exempt
def enter_attendance(request):
	if request.method == 'POST':	 
		a = eval(dict(request.POST).keys()[0])
		print a
		if TeacherProfile.objects.filter(staff_name = a['username']):
			staff = TeacherProfile.objects.get(staff_name = a['username'])
			store = StudentEntries.objects.filter(user = staff,student_id = a['student_id']).update(subject=a['subject'],student_name=a['student_name']) if StudentEntries.objects.filter(user = staff,student_id = a['student_id']) else StudentEntries.objects.create(user = staff,student_id = a['student_id'],subject=a['subject'],student_name=a['student_name'])
		else : 
			new_staff = TeacherProfile.objects.create(staff_name = a['username'])
			new_feed = StudentEntries.objects.filter(user = new_staff,student_id = a['student_id']).update(subject=a['subject'],student_name=a['student_name']) if StudentEntries.objects.filter(user = new_staff,student_id = a['student_id']) else StudentEntries.objects.create(user = new_staff,student_id = a['student_id'],subject=a['subject'],student_name=a['student_name'])
		# objectStore.openCursor().onsuccess = function(event) {
	 #    var cursor = event.target.result;
	 #    console.log(cursor)
		print '???'
	return HttpResponse(content=json.dumps({"data": "api feed"}), content_type='application/json')            

# Create your views here.
