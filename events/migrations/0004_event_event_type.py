# Generated by Django 3.1.2 on 2021-04-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210403_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
