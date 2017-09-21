from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import moodle2.ORM as ORM
from moodle2.dbParams import *


# Create your views here.
def authentication(request, username, password="1234"):
	if 	cur.execute("SELECT `username`, `password` FROM `users` WHERE `username`="Kevinazzzo" AND `password`="1234";") == 1:
		return HttpResponse("<p>TRUE</p>")
	else:
		return HttpResponse("<p>NOPE</p>")

def req_groups(request):
	cur.execute("SELECT * FROM groups;")
	array=[]
	for results in [cur.fetchall()]:
		for row in results:
			id=row['id']
			sname=row['name']
			shift=row['shift']
			desc=row['desc']
			grp = ORM.group(id,sname,shift,desc).__json__()
			array.append(grp)
	json = {'groups': array}
	return JsonResponse(json)