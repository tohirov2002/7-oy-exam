import django_filters

from .views import Commander


class CommanderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', field_name='name')
    did = django_filters.CharFilter(lookup_expr='icontains', field_name='did')
    class Meta:
        model = Commander
        fields = []

