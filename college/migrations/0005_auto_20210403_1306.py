# Generated by Django 3.1.7 on 2021-04-03 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_auto_20210403_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='dep_hod',
        ),
        migrations.AddField(
            model_name='staff',
            name='deptartment_id',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='college.department'),
            preserve_default=False,
        ),
    ]
