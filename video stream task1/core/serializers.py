from rest_framework import serializers
from .models import Video


# video file get ,post,put,dlt
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'path']
