# Generated by Django 4.2.11 on 2024-05-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rides", "0003_alter_person_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
