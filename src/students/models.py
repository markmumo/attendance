import uuid
from django.db import models

# Create your models here. 


COLLEGE_OF_HEALTH_SCIENCES = 'COHES'
SCHOOL_OF_COMPUTING_AND_INFORMATION_TECHNOLOGY = 'SCIT'

DEPARTMENT_TYPE_CHOICES = [
    ('COHES', 'Collage of Health Sciences'),
    ('SCIT', 'School of Computing and Information Technology'),
    ]

class Department(models.Model):
    # INFORMATION_TECHNOLOGY = 'BIT'
    # COLLEGE_OF_HEALTH_SCIENCES = 'COHES'
    # COMPUTER_SCIENCE = 'SCIT'

# DEPARTMENT_TYPE_CHOICES = (
#     (INFORMATION_TECHNOLOGY, 'Information technology'),
#     (COLLEGE_OF_HEALTH_SCIENCES, 'Collage of health sciences'),
#     (COMPUTER_SCIENCE, 'Computer science'),
# )

    # DEPARTMENT_TYPE_CHOICES = [
    #     ('BIT', 'Information technology'),
    #     ('COHES', 'Collage of health sciences'),
    #     ('SCIT', 'Computer science'),
    # ]

    Department_Code = models.CharField(primary_key=True, max_length=10)
  # Department_Name = models.CharField(max_length=200, null=False)
    Department_Type = models.CharField(max_length=200, choices=DEPARTMENT_TYPE_CHOICES, default='SCIT')

# class Meta:
#         verbose_name = ('department')
#         verbose_name_plural = ('departments')
#         ordering = ['dept_code']
    # def __str__(self):
    #     return self.dept_name
    # def __unicode__(self):
    #     return u"{} ({} cfu)".format(self.dept_name, self.dept_code)

class Course(models.Model):
    COURSE_YEAR_CHOICES = (
        (1.1, 'First Year First Semester'),
        (1.2, 'First Year Second Semester'),
        (2.1, 'Second Year First Semester'),
        (2.2, 'Second Year Second Semester'),
        (3.1, 'Third Year First Semester'),
        (3.2, 'Third Year Second Semester'),
        (4.1, 'Fourth Year First Semester'),
        (4.2, 'Fourth Year Second Semester'),
    )
    Unit_Code = models.CharField(primary_key=True, max_length=10)
    Unit_Name = models.CharField(max_length=200, null=False)
    Year = models.IntegerField(choices=COURSE_YEAR_CHOICES, default=0)
    Department = models.ForeignKey(Department, related_name="courses",on_delete=models.PROTECT)

    def __unicode__(self):
        return u"{} ({} cfu)".format(self.Unit_Name, self.Unit_Code)

class Student(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_Name = models.CharField(max_length=255, null=False, blank=False)
    Last_Name = models.CharField(max_length=255, blank=False, null=False)
    Other_Names = models.CharField(max_length=255, null=True, blank=True)
    Registration_Number = models.CharField(unique=True, max_length=20, null=True, blank=False)
  # department = models.ForeignKey(Department, related_name="courses",on_delete=models.PROTECT)
  # id_no_Passport = models.CharField(max_length=255, null=False, blank=False)
  # country = models.CharField(max_length=255, null=True, blank=True)
    Date_of_Birth = models.DateField(blank=False, null=False)
    Image = models.ImageField(null=False ,blank=False, upload_to="profile_images")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    #guid = models.UUIDField(unique=True, default=uuid.uuid4)
    Parent_Contacts = models.CharField(max_length=255, null=False, blank=False)
    Student_Contacts = models.CharField(max_length=255, null=True, blank=True)
    Address = models.CharField(max_length=255, null=False, blank=False)
    Email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    Certificates = models.FileField(blank=False, null=False, upload_to="documents")
    #REQUIRED_FIELDS = ['guid']

    def get_full_name(self):
        return '{} {}'.format(self.First_Name, self.Last_Name)

    def get_short_name(self):
        return self.First_Name

    def __str__(self):
        return self.Registration_Number

