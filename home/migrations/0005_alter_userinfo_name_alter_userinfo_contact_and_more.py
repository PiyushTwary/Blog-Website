# Generated by Django 5.0.1 on 2024-02-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userinfo_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='contact',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
