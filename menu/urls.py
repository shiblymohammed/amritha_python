from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'daily-specials', views.DailySpecialViewSet, basename='dailyspecial')

urlpatterns = [
    path('menu/', include(router.urls)),
]
