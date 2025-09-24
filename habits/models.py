from django.conf import settings
from django.db import models


class Habit(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название привычки",
        help_text="Укажите название привычки",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )
    action = models.TextField(
        verbose_name="Действие",
        help_text="Укажите действие, которое представляет собой привычка",
        null=True,
        blank=True,
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место",
        help_text="Укажите место выполнения привычки",
        null=True,
        blank=True,
    )
    lead_time = models.TimeField(
        verbose_name="Время",
        help_text="Укажите в какое время планируется выполнять привычку",
        null=True,
        blank=True,
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Выберите через сколько дней будите выполнять полезную привычку (1-7)",
    )
    date_last_execution = models.DateField(
        verbose_name="Дата последнего выполнения полезной привычки",
        null=True,
        blank=True,
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Отметьте, что привычка является приятной (вознаграждаемой)",
    )
    associated_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        null=True,
        blank=True,
    )
    reward = models.CharField(
        max_length=255,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение за выполнение привычки",
        null=True,
        blank=True,
    )
    time_for_task = models.PositiveIntegerField(
        verbose_name="Время на выполнение в секундах",
        help_text="Укажите время на выполнения полезной привычки",
        null=True,
        blank=True,
    )
    is_public = models.BooleanField(
        verbose_name="Публиковать привычку",
        help_text="Публичная привычка, доступная другим пользователям",
        default=False,
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["owner", "name"]

    def __str__(self):
        return f"{self.name} (Пользователь: {self.owner})"
