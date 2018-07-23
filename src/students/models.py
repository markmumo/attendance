import uuid
from django.db import models

# Create your models here. 

BUSINESS_COMPUTING = 'BBC'
COLLEGE_OF_HEALTH_SCIENCES = 'COHES'
SCHOOL_OF_COMPUTING_AND_INFORMATION_TECHNOLOGY = 'SCIT'

First_Year_First_Semester = 1.1
First_Year_Second_Semester = 1.2
Second_Year_First_Semester = 2.1
Second_Year_Second_Semester = 2.2
Third_Year_First_Semester = 3.1
Third_Year_Second_Semester = 3.2
Fourth_Year_First_Semester = 4.1
Fourth_Year_Second_Semester = 4.2


DEPARTMENT_TYPE_CHOICES = [
    ('SCIT', 'School of Computing and Information Technology'),
    ('COHES', 'Collage of Health Sciences'),
    ('BBC', 'Business Computing'),
    ]

COURSE_YEAR_CHOICES = (
    (First_Year_First_Semester, 'First Year First Semester'),
    (First_Year_Second_Semester, 'First Year Second Semester'),
    (Second_Year_First_Semester, 'Second Year First Semester'),
    (Second_Year_Second_Semester, 'Second Year Second Semester'),
    (Third_Year_First_Semester, 'Third Year First Semester'),
    (Third_Year_Second_Semester, 'Third Year Second Semester'),
    (Fourth_Year_First_Semester, 'Fourth Year First Semester'),
    (Fourth_Year_Second_Semester, 'Fourth Year Second Semester'),
    )


class Lecturers(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    other_names = models.CharField(max_length=255, null=True, blank=True)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name


class Department(models.Model):
    
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
    # COURSE_YEAR_CHOICES = (
    #     (1.1, 'First Year First Semester'),
    #     (1.2, 'First Year Second Semester'),
    #     (2.1, 'Second Year First Semester'),
    #     (2.2, 'Second Year Second Semester'),
    #     (3.1, 'Third Year First Semester'),
    #     (3.2, 'Third Year Second Semester'),
    #     (4.1, 'Fourth Year First Semester'),
    #     (4.2, 'Fourth Year Second Semester'),
    # )
    # First_Year_First_Semester = 1.1
    # First_Year_Second_Semester = 1.2
    # Second_Year_First_Semester = 2.1
    # Second_Year_Second_Semester = 2.2
    # Third_Year_First_Semester = 3.1
    # Third_Year_Second_Semester = 3.2
    # Fourth_Year_First_Semester = 4.1
    # Fourth_Year_Second_Semester = 4.2

    # COURSE_YEAR_CHOICES = (
    #     (First_Year_First_Semester, 'First Year First Semester'),
    #     (First_Year_Second_Semester, 'First Year Second Semester'),
    #     (Second_Year_First_Semester, 'Second Year First Semester'),
    #     (Second_Year_Second_Semester, 'Second Year Second Semester'),
    #     (Third_Year_First_Semester, 'Third Year First Semester'),
    #     (Third_Year_Second_Semester, 'Third Year Second Semester'),
    #     (Fourth_Year_First_Semester, 'Fourth Year First Semester'),
    #     (Fourth_Year_Second_Semester, 'Fourth Year Second Semester'),
    #     )


    unit_code = models.CharField(primary_key=True, max_length=10)
    unit_name = models.CharField(max_length=200, null=False)
    year = models.IntegerField(choices=COURSE_YEAR_CHOICES, default='First_Year_First_Semester')
    department = models.ForeignKey(Department, related_name="courses",on_delete=models.PROTECT)
    # lecturer = models.ForeignKey(Lecturers, related_name="units_taught",on_delete=models.PROTECT)

    def __unicode__(self):
        return u"{} ({} cfu)".format(self.unit_name, self.unit_code)

class Student(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    other_names = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(unique=True, max_length=20, null=True, blank=False)
    department = models.ForeignKey(Department, related_name="student_course",on_delete=models.PROTECT)
    #year = models.ForeignKey(Course, related_name="student_year", on_delete=models.PROTECT)
    id_no_Passport = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(blank=False, null=False)
    image = models.ImageField(null=False ,blank=False, upload_to="profile_images")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    #guid = models.UUIDField(unique=True, default=uuid.uuid4)
    parent_Contacts = models.CharField(max_length=255, null=False, blank=False)
    student_Contacts = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    certificates = models.FileField(blank=False, null=False, upload_to="documents")
    #REQUIRED_FIELDS = ['guid']

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.registration_number

