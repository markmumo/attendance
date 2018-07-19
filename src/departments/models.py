from django.db import models

# Create your models here.
class Department(models.Model):
    department_code = models.CharField(unique=True, max_length=20, null=True, blank=True)
    department_name = models.CharField(max_length=255, null=False, blank=False)
    
