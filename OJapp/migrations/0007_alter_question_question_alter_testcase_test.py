# Generated by Django 4.0.5 on 2022-07-02 11:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJapp', '0006_testcase_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='test',
            field=models.CharField(choices=[('a', 'r')], max_length=200, null=True),
        ),
    ]
