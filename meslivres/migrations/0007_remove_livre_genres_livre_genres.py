# Generated by Django 4.2.4 on 2023-08-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meslivres', '0006_remove_livre_genres_livre_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='genres',
        ),
        migrations.AddField(
            model_name='livre',
            name='genres',
            field=models.ManyToManyField(to='meslivres.genre'),
        ),
    ]
