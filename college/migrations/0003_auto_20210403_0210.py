# Generated by Django 3.1.7 on 2021-04-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20210403_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='college/staff/'),
        ),
    ]
