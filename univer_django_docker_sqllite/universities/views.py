from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from .models import Task, Result
from .serializers import TaskSerializers, ResultSerializers
import threading
import time
import datetime
from bs4 import BeautifulSoup
import requests as req

# Create your views here.
class AddView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


def parse():
    results = Task.objects.all()
    for result in results:
        resp = req.get("https://www.avito.ru/" + result.region + "/" + result.phrase)
        soup = BeautifulSoup(resp.text, 'lxml') 
        for tag in soup.find_all('span', {'class': 'page-title-count-1oJOc'}):
            task_object = Result(task=result, result=tag.text)
            task_object.save()


class StatView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializers
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


while True:
    time.sleep(1)
    t = threading.Thread(target=parse)
    t.setDaemon(True)
    t.start()
