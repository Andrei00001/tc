from rest_framework import serializers
class SizeSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.IntegerField()


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField()
    sku = serializers.CharField()
    price = serializers.IntegerField()
    brand_name = serializers.CharField()
    size = SizeSerializer(many=True)
