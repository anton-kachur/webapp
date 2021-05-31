from rest_framework import serializers
from .models import Car, Instructor

class CarSerializer(serializers.Serializer):
	carId = serializers.IntegerField()
	carName = serializers.CharField(max_length=20)
	year = serializers.IntegerField()
	number = serializers.CharField(max_length=20)
	
	def create(self, validated_data):
		return Car.objects.create(**validated_data)
		
	def update(self, instance, validated_data):
		instance.carId = validated_data.get('carId', instance.carId)
		instance.carName = validated_data.get('carName', instance.carName)
		instance.year = validated_data.get('year', instance.year)
		instance.number = validated_data.get('number', instance.number)
		instance.save()
		return instance
		
class InstructorSerializer(serializers.Serializer):
	firstName = serializers.CharField(max_length=20)
	lastName = serializers.CharField(max_length=20)
	experience = serializers.FloatField()
	rate = serializers.FloatField()
	
	def create(self, validated_data):
		return Instructor.objects.create(**validated_data)
		
	def update(self, instance, validated_data):
		instance.firstName = validated_data.get('firstName', instance.firstName)
		instance.lastName = validated_data.get('lastName', instance.lastName)
		instance.experience = validated_data.get('experience', instance.experience)
		instance.rate = validated_data.get('rate', instance.rate)
		instance.save()
		return instance