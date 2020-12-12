from rest_framework import serializers
from .models import *

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task

        exclude = ()


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result

        exclude = ()