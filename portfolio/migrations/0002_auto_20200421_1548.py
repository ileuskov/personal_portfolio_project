# Generated by Django 3.0.5 on 2020-04-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='iamge',
            new_name='image',
        ),
    ]
