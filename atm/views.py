from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Account

def index(request):
	return HttpResponse("Hello, world. You're at the atm index.")

def withdraw(request, account_no, amount):
	if self.is_blocked:
		return HttpResponse("Account is blocked")
	
	if self.balance < amount:
		return HttpResponse("Insufficient balance")

	self.balance = self.balance - amount
	self.save()
	
	return HttpResponse("Rs. " + str(amount) + " withdrawl success, " + "new balance is Rs. " + str(self.balance))
