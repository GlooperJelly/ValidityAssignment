from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from emails.serailzers import EmailSerializer
from rest_framework import viewsets
from emails.models import Email


def index(request):
    return HttpResponse("Hello, world")

class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer