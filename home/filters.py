import django_filters
from django_filters import DateFilter
from .models import Product

class ProductFilter(django_filters.FilterSet):
    
    date_created = DateFilter(field_name='date_created', lookup_expr='date')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['name', 'status',  'quantity', 'unit', 'user', 'date_created', 'updated']