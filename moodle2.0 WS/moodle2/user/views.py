from django.shortcuts import render
from django.http import JsonResponse
import moodle2.ORM as ORM
# Create your views here.
# Views Handles web service JSON responses

def sdad(request):
	arg1="hola"
	json1  = JSONEncoder.encode(arg1)
	return json1.__str__
def test(request):
	course1 = ORM.course(1,"Math","Kaeko")
	return JsonResponse(course1.__json__())
	