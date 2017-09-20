from django.shortcuts import render
from moodle2 import dbParams as connection


# Create your views here.
def authentication(request, usr, pwd):
	connection.cur.ex