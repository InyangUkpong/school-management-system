# Generated by Django 4.2.1 on 2023-05-21 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studentclassinfo_class_short_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='class_type',
            field=models.CharField(choices=[('software', 'Software Engineering'), ('data analytics', 'Data Analytics'), ('aws cloud', 'AWS Cloud Practitioner')], max_length=30),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='fathers_img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='fathers_nid',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='fathers_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mothers_img',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mothers_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mothers_nid',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mothers_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='section_type',
            field=models.CharField(choices=[('cohort 5', 'Cohort 5'), ('cohort 6', 'Cohort 6'), ('cohort 7', 'Cohort 7'), ('cohort 8', 'Cohort 8'), ('cohort 9', 'Cohort 9')], max_length=30),
        ),
    ]