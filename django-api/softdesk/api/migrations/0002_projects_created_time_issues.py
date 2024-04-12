# Generated by Django 5.0.4 on 2024-04-12 16:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="projects",
            name="created_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Issues",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("LOW", "Low"),
                            ("MEDIUM", "Medium"),
                            ("HIGH", "High"),
                        ],
                        max_length=9,
                    ),
                ),
                (
                    "issue_type",
                    models.CharField(
                        choices=[
                            ("BUG", "Bug"),
                            ("FEATURE", "Feature"),
                            ("TASK", "Task"),
                        ],
                        max_length=7,
                    ),
                ),
                (
                    "progress",
                    models.CharField(
                        choices=[
                            ("To Do", "Todo"),
                            ("In Progress", "In Progress"),
                            ("Finished", "Finished"),
                        ],
                        max_length=11,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
                (
                    "assignment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_to",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "author_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.projects"
                    ),
                ),
            ],
        ),
    ]