# Generated by Django 4.0.5 on 2022-06-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJapp', '0002_testcase_expectedoutput_testcase_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='ExpectedOutput',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='Input',
            field=models.TextField(max_length=200),
        ),
    ]
