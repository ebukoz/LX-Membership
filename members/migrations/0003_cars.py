# Generated by Django 4.2.4 on 2023-08-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mileage', models.IntegerField(null=True)),
                ('manufacturer', models.CharField(max_length=255)),
                ('year', models.IntegerField(null=True)),
            ],
        ),
    ]
