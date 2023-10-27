# Generated by Django 4.2.5 on 2023-10-04 10:15

import coreapp.models.scratch
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0039_alter_scratch_libraries"),
    ]

    operations = [
        migrations.CreateModel(
            name="Preset",
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
                ("creation_time", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("platform", models.CharField(max_length=100)),
                ("compiler", models.CharField(max_length=100)),
                (
                    "assembler_flags",
                    models.TextField(blank=True, default="", max_length=1000),
                ),
                (
                    "compiler_flags",
                    models.TextField(blank=True, default="", max_length=1000),
                ),
                ("diff_flags", models.JSONField(default=list)),
                (
                    "decompiler_flags",
                    models.TextField(blank=True, default="", max_length=1000),
                ),
                ("libraries", coreapp.models.scratch.LibrariesField(default=list)),
            ],
            options={
                "ordering": ["-creation_time"],
            },
        ),
        migrations.RemoveField(
            model_name="projectfunction",
            name="import_config",
        ),
        migrations.DeleteModel(
            name="ProjectImportConfig",
        ),
    ]
