from rest_framework import serializers
from .models import DailySpecial

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySpecial
        fields = "__all__"
