# Generated by Django 2.0.7 on 2018-07-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_attendence'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('excused', 'Excused')], default='', max_length=10),
        ),
    ]