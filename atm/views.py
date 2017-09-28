import time
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Account

def index(request):
	return JsonResponse({'response' : "Hello, world. You're at the atm index."})

def withdraw(request, account_no, amount):
	if self.is_blocked:
		return JsonResponse({'response' : "Account is blocked"})
	
	if self.balance < amount:
		return JsonResponse({'response' : "Insufficient balance"})

	self.balance = self.balance - amount
	self.save()
	
	response = {'account':{'account_no' : account_no, 'account_holder_name' : self.account_holder_name, 'balance' : self.balance},
	'transaction_detail' : {'last_transaction' : {'time':time.localtime()}}}
	
	return JsonResponse(response)
