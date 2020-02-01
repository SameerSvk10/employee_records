from .models import Employee
from datetime import datetime, timedelta
from django.utils.timezone import get_current_timezone

import random

departments = ['D1', 'D2' 'D3', 'D4', 'D5', 'D6', 'Waltzz', 'D7']

"""
This method creates random employee records in Employee table
"""


def create_employee_records():
    for i in range(1, 200):
        employee = Employee()
        employee.department = random.choice(departments)
        employee.score = random.randint(1, 100)
        employee.employee_code = 'E' + str(i)
        employee.date_created = datetime.now(tz=get_current_timezone()) - timedelta(days=random.randint(0, 60))
        employee.save()
