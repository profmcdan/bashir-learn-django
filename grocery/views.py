from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
# Create your views here.


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
