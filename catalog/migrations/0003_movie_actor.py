# Generated by Django 2.2.3 on 2019-07-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(help_text='Select a actor for this movie', to='catalog.Actor'),
        ),
    ]
