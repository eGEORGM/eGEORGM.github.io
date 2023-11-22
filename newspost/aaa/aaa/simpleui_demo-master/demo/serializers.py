from rest_framework import serializers
from .models import News
# serializers.py (在您的应用目录中)

from rest_framework import serializers
from .models import Image, News

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['title', 'image', 'image_url']

    def get_image_url(self, obj):
        # 返回图片的完整 URL
        return obj.image.url if obj.image else None


class NewsSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'uploadtime', 'context', 'type', 'image']
