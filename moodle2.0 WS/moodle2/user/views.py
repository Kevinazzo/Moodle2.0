from django.shortcuts import render
from django.http import JsonResponse
import moodle2.ORM as ORM
from moodle2.dbParams import *
# Create your views here.
# Views Handles web service JSON responses

def sdad(request):
	arg1="hola"
	json1  = JSONEncoder.encode(arg1)
	return json1.__str__

def test(request):
	response = ORM.course(1,"Math","Kaeko")
	return JsonResponse(response.__json__())

