# Generated by Django 5.0.1 on 2024-02-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_userinfo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
