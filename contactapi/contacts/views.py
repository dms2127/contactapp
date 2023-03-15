from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import permissions 
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

class Contactlist(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self , serializer):
        serializer.save(owner = self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner = self.request.user)

class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id" 


    def get_queryset(self):
        return Contact.objects.filter(owner = self.request.user)


def index(request):
    key = Contact.objects.all()
    return render(request, 'index.html',{'data':key})

