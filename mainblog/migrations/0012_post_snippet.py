# Generated by Django 3.2.15 on 2022-08-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0011_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read...', max_length=255),
        ),
    ]