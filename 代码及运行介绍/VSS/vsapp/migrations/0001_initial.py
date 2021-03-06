# Generated by Django 2.2.7 on 2021-04-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=500)),
                ('situation', models.CharField(max_length=200)),
                ('later', models.CharField(max_length=500)),
                ('position', models.CharField(max_length=500)),
                ('province', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('AnnualSalary', models.CharField(max_length=500)),
            ],
        ),
    ]
