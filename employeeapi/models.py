from django.db import models
from django.utils import timezone


class Employee(models.Model):
    employee_code = models.CharField(max_length=50, primary_key=True)
    department = models.CharField(max_length=50)
    score = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "Employee"

    def __str__(self):
        return self.employee_code
