from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car, Instructor
from .serializers import CarSerializer, InstructorSerializer

class CarView(APIView):
	def get(self, request, pk):
		cars = Car.objects.all()
		serializer = CarSerializer(cars, many=True)
		return Response({"cars": serializer.data})
	
	def post(self, request, pk):
		car = request.data.get('car')
		# Create an article from the above data
		serializer = CarSerializer(data=car)
		if serializer.is_valid(raise_exception=True):
			car_saved = serializer.save()
		return Response({"success": "Car '{}' created successfully".format(car_saved.carName)})
		
	def put(self, request, pk):
		saved_car = get_object_or_404(Car.objects.all(), pk=pk)
		data = request.data
		serializer = CarSerializer(instance=saved_car, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			car_saved = serializer.save()
		return Response({"success": "Car '{}' updated successfully".format(car_saved.carName)})
	
	def delete(self, request, pk):
		# Get object with this pk
		car = get_object_or_404(Car.objects.all(), pk=pk)
		car.delete()
		return Response({"message": "Car with id `{}` has been deleted.".format(pk)
		}, status=204)
		
		
class InstructorView(APIView):
	def get(self, request, pk):
		instructors = Instructor.objects.all()
		serializer = InstructorSerializer(instructors, many=True)
		return Response({"instructors": serializer.data})
		
	def post(self, request, pk):
		instructor = request.data.get("instructor")
		# Create an article from the above data
		serializer = InstructorSerializer(data=instructor)
		if serializer.is_valid(raise_exception=True):
			instructor_saved = serializer.save()
		return Response({"success": "Instructor '{}' created successfully".format(instructor_saved.firstName)})
		
	def put(self, request, pk):
		saved_instructor = get_object_or_404(Instructor.objects.all(), pk=pk)
		data = request.data.get('instructor')
		serializer = InstructorSerializer(instance=saved_instructor, data=data, partial=True)
		if serializer.is_valid(raise_exception=True):
			instructor_saved = serializer.save()
		return Response({"success": "Instructor '{}' updated successfully".format(instructor_saved.firstName)})

	def delete(self, request, pk):
		# Get object with this pk
		instructor = get_object_or_404(Instructor.objects.all(), pk=pk)
		instructor.delete()
		return Response({"message": "Instructor with id `{}` has been deleted.".format(pk)
		}, status=204)