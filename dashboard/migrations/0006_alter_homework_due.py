# Generated by Django 4.2.6 on 2024-01-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_homework_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateField(),
        ),
    ]
