# Generated by Django 3.2.15 on 2022-12-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0015_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]