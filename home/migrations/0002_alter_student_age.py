# Generated by Django 4.1.1 on 2022-10-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
