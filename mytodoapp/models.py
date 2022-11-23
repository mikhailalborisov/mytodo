from django.db import models
from django.urls import reverse


class ToDo(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите наименнование задачи",
        verbose_name="Название задачи",
    )
    description = models.CharField(
        max_length=200,
        help_text="Введите описание задачи",
        verbose_name="Описание задачи",
    )
    created_at = models.DateField(
        null=True,
        blank=True,
        help_text="Введите дату создания задачи",
        verbose_name="Дата создания задачи",
    )
    resolved_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Введите дату выполнения задачи",
        verbose_name="Дата выполнения задачи",
    )
    status = models.BooleanField(
        default=False,
        help_text="Отметьте статус задачи",
        verbose_name="Статус задачи",
    )
