from django.db import models
from django.core.validators import MinValueValidator


class GeneticTest(models.Model):
    class HealthStatus(models.TextChoices): 
        GOOD = 'GOOD', 'Good'
        POOR = 'POOR', 'Poor'

    animal_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    test_date = models.DateField()
    milk_yield = models.FloatField(validators=[MinValueValidator(0.0, message="Продуктивность должна быть положительным числом")])
    health_status = models.CharField(max_length=4, choices=HealthStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Генетический тест'
        verbose_name_plural = 'Генетические тесты'

    def __str__(self):
        return f"{self.animal_name} ({self.species}) - {self.test_date}"
