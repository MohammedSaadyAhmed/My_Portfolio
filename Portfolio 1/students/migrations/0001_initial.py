# Generated by Django 4.2.1 on 2023-05-14 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_Name', models.CharField(max_length=255)),
                ('l_Name', models.CharField(max_length=255)),
            ],
        ),
    ]
