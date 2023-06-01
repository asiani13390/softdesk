# Generated by Django 4.2.1 on 2023-06-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issue_tracking_system", "0024_alter_project_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issue",
            name="priority",
            field=models.CharField(
                choices=[("LOW", "Low"), ("MEDIUM", "Medium"), ("HIGH", "High")],
                max_length=255,
            ),
        ),
    ]
