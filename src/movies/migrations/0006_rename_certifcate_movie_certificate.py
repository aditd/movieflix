# Generated by Django 3.2.8 on 2021-10-28 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_certifcate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='certifcate',
            new_name='certificate',
        ),
    ]
