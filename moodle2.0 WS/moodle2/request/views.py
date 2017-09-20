from django.shortcuts import render
import moodle2.ORM as ORM
from moodle2.dbParams import *


# Create your views here.
def authentication(request, usr, pwd):
	if 	cur.execute("SELECT username, pwd FROM user WHERE `username`="+usr+"AND `password="+pwd) == 1:
		return True
	else:
		return False

def groups(request):
	cur._query("SELECT * FROM group WHERE id")