# Generated by Django 3.2.15 on 2022-12-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0013_userprofile_instagram_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Computer Science', max_length=200),
        ),
    ]