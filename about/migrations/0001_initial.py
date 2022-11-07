# Generated by Django 4.1.2 on 2022-11-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Employee Name')),
                ('role', models.CharField(max_length=60, verbose_name='Employee Role')),
                ('description', models.TextField(blank=True, verbose_name='Employee Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/static/employee_images/')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
