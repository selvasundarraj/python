---serializers.py---
from rest_framework import serializers
from .models import BundleCSV

class BundleCSVSerializer(serializers.ModelSerializer):
    class Meta:
        model = BundleCSV
        fields = '__all__'

--views.py---

from rest_framework import viewsets
from .models import BundleCSV
from .serializers import BundleCSVSerializer

class BundleCSVViewSet(viewsets.ModelViewSet):
    queryset = BundleCSV.objects.all()
    serializer_class = BundleCSVSerializer

--urls.py---
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BundleCSVViewSet

router = DefaultRouter()
router.register(r'bundlecsv', BundleCSVViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
