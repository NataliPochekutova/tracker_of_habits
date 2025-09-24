from rest_framework import serializers

from habits.models import Habit
from habits.validators import (associated_habit_is_nice_habit_validator,
                               associated_habit_or_reward_validator,
                               is_nice_habit_validator)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели привычка"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            associated_habit_or_reward_validator,
            associated_habit_is_nice_habit_validator,
            is_nice_habit_validator,
        ]

    def validate_time_for_task(self, value):
        """Валидатор для проверки, что время выполнения не больше 120 секунд."""
        if value is not None and value > 120:
            raise serializers.ValidationError(
                "Время выполнения должно быть не больше 120 секунд."
            )
        return value

    def validate_periodicity(self, value):
        """Валидатор для проверки, что привычка выполняется не реже, чем 1 раз в 7 дней."""
        if not (1 <= value <= 7):
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
        return value
