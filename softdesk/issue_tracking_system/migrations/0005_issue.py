# Generated by Django 4.2.1 on 2023-05-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issue_tracking_system", "0004_delete_issue"),
    ]

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("desc", models.CharField(max_length=255)),
                ("tag", models.CharField(max_length=255)),
                ("priority", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("created_time", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Issues",
            },
        ),
    ]
