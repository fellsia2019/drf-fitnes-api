# Generated by Django 4.2 on 2023-04-18 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fitnes", "0004_session_title"),
    ]

    operations = [
        migrations.RemoveField(model_name="session", name="direction",),
        migrations.AddField(
            model_name="catsession",
            name="direction",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="fitnes.catdirection",
            ),
        ),
    ]
