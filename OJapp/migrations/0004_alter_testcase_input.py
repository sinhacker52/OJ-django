# Generated by Django 4.0.5 on 2022-06-28 17:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJapp', '0003_alter_testcase_expectedoutput_alter_testcase_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='Input',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]