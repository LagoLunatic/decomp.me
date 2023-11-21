# Generated by Django 4.2.6 on 2023-10-24 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("coreapp", "0042_migrate_presets_to_db"),
    ]

    operations = [
        migrations.AddField(
            model_name="scratch",
            name="preset_fk",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="coreapp.preset",
            ),
        ),
    ]