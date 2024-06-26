# Generated by Django 5.0.4 on 2024-05-10 03:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_projects_project_type"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="contributors",
            field=models.ManyToManyField(
                through="api.Contributors", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="contributors",
            name="projects_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="project",
                to="api.projects",
            ),
        ),
        migrations.AlterField(
            model_name="projects",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="projects",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("Back-End", "Back End"),
                    ("Front-End", "Front End"),
                    ("iOS", "Ios"),
                    ("Android", "Android"),
                ],
                max_length=9,
            ),
        ),
    ]
