from .models import Employee
from .serializers import EmployeeSerializer

from datetime import datetime, timedelta
from django.utils.timezone import get_current_timezone

import itertools


def get_all_employees():
    queryset = Employee.objects.all().order_by('-score')
    serializer_class = EmployeeSerializer(queryset, many=True)
    employees = serializer_class.data
    return employees


def get_employees_by_department(department='Waltzz'):
    queryset = Employee.objects.filter(department=department)
    return queryset


def get_recently_added_employees(days=14, department='Waltzz'):
    date_n_days_ago = datetime.now(tz=get_current_timezone()) - timedelta(days=days)
    queryset = Employee.objects.filter(date_created__gte=date_n_days_ago).exclude(department=department)
    return queryset


def get_rest_of_the_employees(days=14, department='Waltzz'):
    date_n_days_ago = datetime.now(tz=get_current_timezone()) - timedelta(days=days)

    queryset = Employee.objects.exclude(department=department).exclude(date_created__gt=date_n_days_ago).order_by(
        '-score')

    return queryset


"""

get employees object in given format
This method gets 3 querysets
    1. get all employees except from 'Waltzz' department and the ones recently added( < 14 days)
    2. get all employees from 'Waltzz' department
    3. get all employees added in last 14 days except that belong to 'Waltzz' department
 and iterates over them using itertools's zip longest function
 
 This method also accepts optional parameter 'chunk';
 when it is not None it sends employee results batch of 20
 
"""


def get_employee_records(chunk=None):
    all_employee_query_set = iter(get_rest_of_the_employees())
    department_employee_query_set = iter(get_employees_by_department())
    recently_added_employee_query_set = iter(get_recently_added_employees())
    employee_list = list(itertools.chain(
        *itertools.zip_longest(all_employee_query_set, all_employee_query_set, all_employee_query_set,
                               all_employee_query_set, department_employee_query_set, department_employee_query_set,
                               recently_added_employee_query_set, recently_added_employee_query_set,
                               fillvalue=Employee())))

    serializer_class = EmployeeSerializer(employee_list, many=True)
    employees = serializer_class.data

    if chunk is not None and chunk.isnumeric():
        chunk = int(chunk)
        start_index = 20 * chunk - 20
        end_index = start_index + 20
        employees = employees[start_index:end_index]

    employee_object = {"employees": employees}

    return employee_object
