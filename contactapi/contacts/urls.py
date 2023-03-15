from django.urls import path
from .views import Contactlist , ContactDetailView 
from contacts import views


urlpatterns = [
    path('',Contactlist.as_view()),
    path('<int:id>', ContactDetailView.as_view()),
    
]
