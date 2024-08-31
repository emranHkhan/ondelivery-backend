from rest_framework import generics
from django_filters import rest_framework as filters
from .models import FoodItem
from .serializers import FoodItemSerializer

class FoodItemFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category', lookup_expr='iexact')

    class Meta:
        model = FoodItem
        fields = ['category']

class FoodItemListView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FoodItemFilter

class FoodItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
