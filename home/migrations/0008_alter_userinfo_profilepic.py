# Generated by Django 5.0.1 on 2024-02-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_userinfo_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profilePic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='ProfilePic/'),
        ),
    ]