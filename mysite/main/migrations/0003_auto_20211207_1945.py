# Generated by Django 2.2.12 on 2021-12-07 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211207_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='datum_izdavanja_albuma',
        ),
        migrations.RemoveField(
            model_name='pjesma',
            name='datum_izdavanja_pjesme',
        ),
        migrations.AddField(
            model_name='album',
            name='godina_izdavanja_albuma',
            field=models.CharField(default='2021', max_length=4),
        ),
        migrations.AddField(
            model_name='pjesma',
            name='godina_izdavanja_pjesme',
            field=models.CharField(default='2021', max_length=4),
        ),
    ]