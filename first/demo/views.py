from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Another(View):
	def get(self, request):
		return HttpResponse('First message from class views')

def first(request):
	return HttpResponse('First message from views')
