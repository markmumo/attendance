# Generated by Django 2.0.7 on 2018-07-25 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_attendence_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='is_leave',
            new_name='absent_with_reason',
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='image',
        ),
        migrations.RemoveField(
            model_name='attendence',
            name='leave_count',
        ),
    ]