from django.db import models

# Create your models here.

class Car(models.Model):
	carId = models.IntegerField()
	carName = models.CharField(max_length=20)
	year = models.IntegerField()
	number = models.CharField(max_length=20)
	
	def __str__(self):
		return self.carName
		

class Instructor(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	experience = models.FloatField()
	rate = models.FloatField()
	
	def __str__(self):
		return self.firstName