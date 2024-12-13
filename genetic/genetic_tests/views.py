from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg, Max, Q
from .models import GeneticTest
from .serializers import GeneticTestSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class GeneticTestViewSet(viewsets.ModelViewSet):
    """
    API endpoint для управления генетическими тестами животных.
    """
    queryset = GeneticTest.objects.all()
    serializer_class = GeneticTestSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='species',
                description='Фильтрация по виду животного',
                required=False,
                type=str
            )
        ]
    )
    def get_queryset(self):
        queryset = GeneticTest.objects.all()
        species = self.request.query_params.get('species', None)
        if species is not None:
            queryset = queryset.filter(species=species)
        return queryset

    @extend_schema(
        description='Получение агрегированной статистики по видам животных',
        responses={200: {
            'type': 'object',
            'properties': {
                'statistics': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'species': {'type': 'string'},
                            'total_tests': {'type': 'integer'},
                            'avg_milk_yield': {'type': 'number'},
                            'max_milk_yield': {'type': 'number'},
                            'good_health_percentage': {'type': 'number'}
                        }
                    }
                }
            }
        }}
    )
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        species_stats = (
            GeneticTest.objects.values('species')
            .annotate(
                total_tests=Count('id'),
                avg_milk_yield=Avg('milk_yield'),
                max_milk_yield=Max('milk_yield'),
                good_health_count=Count('id', filter=Q(health_status='GOOD'))
            )
        )

        statistics = []
        for stat in species_stats:
            good_health_percentage = (
                (stat['good_health_count'] / stat['total_tests']) * 100
                if stat['total_tests'] > 0 else 0
            )
            
            statistics.append({
                'species': stat['species'],
                'total_tests': stat['total_tests'],
                'avg_milk_yield': round(stat['avg_milk_yield'], 2),
                'max_milk_yield': stat['max_milk_yield'],
                'good_health_percentage': round(good_health_percentage, 2)
            })

        return Response({'statistics': statistics})
