from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet
from .views_auth import RegistroView
router = DefaultRouter()
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroView.as_view(), name='registro'),
]
