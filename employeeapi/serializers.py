# serializers.py
from .models import Employee

from rest_framework import serializers


# this call serializes Django model object into dict with mentioned fields
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('employee_code', 'department', 'score')
