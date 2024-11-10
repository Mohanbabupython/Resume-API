#To connecting MYSQL table with table name..
from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    qualification = models.CharField(max_length=255)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2)
    role = models.CharField(max_length=255)

    class Meta:
        db_table = 'custom_resume_table'  #table name
