# Generated by Django 3.2.5 on 2023-05-27 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracking_system', '0014_auto_20230527_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issue_tracking_system.project'),
        ),
    ]
