import django_filters
from apps.crud_alumnos.models import alumnos,estado


class alumnosFilter(django_filters.FilterSet):
    class Meta:
        model = alumnos
        fields = ['nocontrol', 'nombre', 'carrera']

class estadoFilter(django_filters.FilterSet):
    class Meta:
        model = estado
        fields = ['nombre_estado']
