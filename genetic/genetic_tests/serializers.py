from rest_framework import serializers
from .models import GeneticTest


class GeneticTestSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели генетических тестов.
    
    Поля:
    - animal_name: имя животного
    - species: вид животного
    - test_date: дата проведения теста
    - milk_yield: продуктивность (должна быть положительным числом)
    - health_status: состояние здоровья (GOOD или POOR)
    - created_at: дата создания записи (только для чтения)
    """
    
    class Meta:
        model = GeneticTest
        fields = ['id', 'animal_name', 'species', 'test_date', 'milk_yield', 'health_status', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_health_status(self, value):
        if value not in ['GOOD', 'POOR']:
            raise serializers.ValidationError("Статус здоровья должен быть 'GOOD' или 'POOR'")
        return value