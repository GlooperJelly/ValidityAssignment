# Generated by Django 3.2.12 on 2022-03-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_rename_subjet_email_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='subject',
            field=models.CharField(max_length=500),
        ),
    ]