# Generated by Django 4.2.5 on 2023-10-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_content_content_file_alter_content_fk_syllabus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_file',
            field=models.FileField(upload_to=''),
        ),
    ]
