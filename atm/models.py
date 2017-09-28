from django.db import models

class Account(models.Model):
	account_no = models.IntegerField(default=0)
	account_holder_name = models.CharField(max_length=200)
	balance = models.IntegerField(default=0)
	is_blocked = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.account_no)
