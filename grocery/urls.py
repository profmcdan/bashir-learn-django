from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryView, ItemView

app_name = 'grocery'
router = DefaultRouter()

router.register('category', CategoryView)
router.register('item', ItemView)


urlpatterns = [
    path('', include(router.urls)),
]
