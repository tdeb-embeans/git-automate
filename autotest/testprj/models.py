from django.db import models

# Create your models here.

class TestCase(models.Model):
	test_case_id = models.CharField(max_length=200)
	date_time = models.DateTimeField('date time executed')
	result = models.CharField(max_length=200)
	tag = models.CharField(max_length=200)
	branch = models.CharField(max_length=200)
		
