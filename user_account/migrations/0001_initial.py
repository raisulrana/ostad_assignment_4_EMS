# Generated by Django 5.1.2 on 2024-10-26 18:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("username", models.CharField(blank=True, max_length=50, null=True)),
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "email_address",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "mailing_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]