from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	##return HttpResponse("hello world")
	return render(request, 'home.html', {'name': 'Aaron'})

def add(request):

	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])

	res = val1 + val2

	return render(request, 'results.html', {'result':res})

def study(request):

	val1 = int(request.POST['studyNum'])

	res = 4 + val1

	return render(request, 'studyResults.html', {'result':res})

def workout(request):

	val1 = int(request.POST['workoutNum'])

	res = 7 + val1

	return render(request, 'workoutResults.html', {'result':res})