# Generated by Django 4.2.5 on 2023-10-23 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_student_profilepicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='profilePicture',
            new_name='studentprofilePicture',
        ),
    ]
