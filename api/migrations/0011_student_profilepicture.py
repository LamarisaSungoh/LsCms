# Generated by Django 4.2.5 on 2023-10-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_instructor_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profilePicture',
            field=models.ImageField(blank=True, default=1, null=True, upload_to=''),
        ),
    ]
