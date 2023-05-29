from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'phone_no', 'comp_name', 'designation', 'location', 'image']