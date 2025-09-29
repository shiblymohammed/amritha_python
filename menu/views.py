from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import DailySpecial
from .serializers import DailySpecialSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class DailySpecialViewSet(viewsets.ModelViewSet):
    queryset = DailySpecial.objects.all().order_by("-created_at")
    serializer_class = DailySpecialSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=["get"], url_path="active")
    def active_specials(self, request):
        qs = DailySpecial.objects.filter(is_active=True).order_by("-updated_at")
        serializer = self.get_serializer(qs, many=True)
        return Response({"results": serializer.data})
