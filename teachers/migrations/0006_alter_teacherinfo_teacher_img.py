# Generated by Django 4.2.1 on 2023-05-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_alter_teacherinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='teacher_img',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]