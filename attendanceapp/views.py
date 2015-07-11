from attendanceapp.models import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt,ensure_csrf_cookie
import json,os

@csrf_exempt
def enter_attendance(request):
	print request
	# c = {}
 #    c = csrf(request)
    # return redirect("search.html", c)
	print '???'
	return 'nothing'

# Create your views here.
