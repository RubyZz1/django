# Generated by Django 4.2.4 on 2023-08-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meslivres', '0007_remove_livre_genres_livre_genres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='livre',
            name='genres',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]