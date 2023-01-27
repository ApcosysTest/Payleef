# Generated by Django 4.1.3 on 2023-01-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companysetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, unique=True)),
                ('website', models.CharField(blank=True, max_length=500, null=True)),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=500, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
                ('companylogo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'companysetup',
            },
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_code', models.CharField(max_length=500)),
                ('emp_Name', models.CharField(max_length=500)),
                ('emp_PAN', models.CharField(max_length=500)),
                ('Joining_date', models.CharField(max_length=500)),
                ('mobile_no', models.IntegerField()),
                ('salary', models.CharField(max_length=500)),
                ('CTC', models.CharField(max_length=500)),
                ('designation', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('bank_Name', models.CharField(max_length=500)),
                ('bank_Account_No', models.CharField(max_length=500)),
                ('IFSC', models.CharField(max_length=500)),
                ('branch', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.EmailField(max_length=10)),
            ],
            options={
                'db_table': 'login',
            },
        ),
    ]