from rest_framework import serializers

from app.models import Price, Size, Product


class SizeSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField()

    class Meta:
        model = Size
        fields = (
            'title',
            'price',
        )


class ProductSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=True)
    brand_name = serializers.CharField()
    price = serializers.IntegerField(source='min_price')

    class Meta:
        model = Product
        fields = (
            'title',
            'sku',
            'price',
            'brand_name',
            'size',
        )