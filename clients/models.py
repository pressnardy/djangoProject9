from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=50)
	policy_number = models.CharField(max_length=50)
	registration_number = models.CharField(max_length=50)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	renewal_date = models.DateField(null=True)
	amount = models.DecimalField(max_digits=10, decimal_places=4)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None, blank=True)


	def __str__(self):
		return f"{self.name}, {self.policy_number}, {self.registration_number}, " \
			   f"{self.start_date}, {self.end_date}, {self.amount}"

