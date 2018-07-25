import uuid
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here. 

BUSINESS_COMPUTING = 'BBC'
COLLEGE_OF_HEALTH_SCIENCES = 'COHES'
SCHOOL_OF_COMPUTING_AND_INFORMATION_TECHNOLOGY = 'SCIT'

DEPARTMENT_TYPE_CHOICES = [
    ('SCIT', 'School of Computing and Information Technology'),
    ('COHES', 'Collage of Health Sciences'),
    ('BBC', 'Business Computing'),
    ]

class Department(models.Model):
    
    Department_Code = models.CharField(primary_key=True, max_length=10) 
    Department_Type = models.CharField(max_length=200, choices=DEPARTMENT_TYPE_CHOICES, default='SCIT')

    def __str__(self):
        return u'%s %s'  % (self.Department_Code, self.Department_Type)

class Course(models.Model):

    COURSE_YEAR_CHOICES = (
        ('First_Year_First_Semester', 'First Year First Semester'),
        ('First_Year_Second_Semester', 'First Year Second Semester'),
        ('Second_Year_First_Semester', 'Second Year First Semester'),
        ('Second_Year_Second_Semester', 'Second Year Second Semester'),
        ('Third_Year_First_Semester', 'Third Year First Semester'),
        ('Third_Year_Second_Semester', 'Third Year Second Semester'),
        ('Fourth_Year_First_Semester', 'Fourth Year First Semester'),
        ('Fourth_Year_Second_Semester', 'Fourth Year Second Semester'),
        )

    unit_code = models.CharField(primary_key=True, max_length=10)
    unit_name = models.CharField(max_length=200, null=False)
    year = models.CharField(max_length=200, choices=COURSE_YEAR_CHOICES, default='First_Year_First_Semester')
    department = models.ForeignKey(Department, related_name="courses",on_delete=models.PROTECT)

    def __str__(self):
        return u'%s %s %s' % (self.unit_code, self.unit_name, self.department)

class Lecturers(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    other_names = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department, related_name="lecturer_courses",on_delete=models.PROTECT)

    def __str__(self):
        return u'%s %s %s' % (self.first_name, self.last_name, self.department)

class Student(models.Model):
   #guid = models.UUIDField(unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    other_names = models.CharField(max_length=255, null=True, blank=True)
    registration_number = models.CharField(unique=True, max_length=20, null=True, blank=False)
    department = models.ForeignKey(Department, related_name="student_course",on_delete=models.PROTECT)
    id_no_Passport = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(blank=False, null=False)
    image = models.ImageField(null=False ,blank=False, upload_to="profile_images")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    parent_Contacts = models.CharField(max_length=255, null=False, blank=False)
    student_Contacts = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    certificates = models.FileField(blank=False, null=False, upload_to="documents")

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return u'%s %s %s %s %s' % (self.first_name, self.last_name, self.registration_number, self.department, self.image)

class Attendence(models.Model):
    
    ATTENDANCE_TYPES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('excused', 'Excused'),
    )
    registration_number = models.ForeignKey(Student,related_name="stud_reg",on_delete=models.PROTECT)
    department = models.ForeignKey(Department, related_name="course_att",on_delete=models.PROTECT)
    unit_name = models.ForeignKey(Course, related_name="unit_att",on_delete=models.PROTECT)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=ATTENDANCE_TYPES, default='')
    absent_with_reason = models.BooleanField(default=False)
    detail = models.TextField(default='no')


    def __str__(self):
        return u'%s %s %s %s %s' % (self.registration_number, self.department, self.unit_name, self.date, self.unit_name)
