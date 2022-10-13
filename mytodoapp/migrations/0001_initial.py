# Generated by Django 4.1.2 on 2022-10-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ToDo",
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
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименнование задачи",
                        max_length=50,
                        verbose_name="Название задачи",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="Введите описание задачи",
                        max_length=200,
                        verbose_name="Описание задачи",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату создания задачи",
                        null=True,
                        verbose_name="Дата создания задачи",
                    ),
                ),
                (
                    "resolved_at",
                    models.DateField(
                        blank=True,
                        help_text="Введите дату выполнения задачи",
                        null=True,
                        verbose_name="Дата выполнения задачи",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=False,
                        help_text="Введите статус задачи",
                        verbose_name="Статус задачи",
                    ),
                ),
            ],
        ),
    ]