# Generated by Django 3.2.8 on 2021-10-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='big_poster_url',
            field=models.SlugField(max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='icon_url',
            field=models.SlugField(max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.SlugField(max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='certifcate',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
