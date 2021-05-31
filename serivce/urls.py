from django.urls import path

from .views import CarView, InstructorView

app_name = "serivce"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('cars/', CarView.as_view()),
	path('instructors/', InstructorView.as_view()),
	path('cars/<int:pk>', CarView.as_view()),
	path('instructors/<int:pk>', InstructorView.as_view())
]