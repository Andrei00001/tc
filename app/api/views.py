from django.db.models import F
from rest_framework import views

from app.api import serializer
from rest_framework.response import Response

from app.models import Product, Price


class ProductView(views.APIView):
    serializer_class = serializer.ProductSerializer

    def get(self, request, sku: str, *args, **kwargs):
        product = Product.objects.filter(sku=sku).first()

        if not product:
            return Response({'attention': f'no data found with this sku - {sku}'})

        prices = Price.objects.annotate(
            title=F('size__title')
        ).filter(
            size__in=product.size.all()
        ).order_by('price').values('title', 'price')

        return Response(
            {
                'title': product.title,
                'sku': product.sku,
                'price': prices[0]['price'],
                'brand_name': product.brand.title,
                'size': prices
            }
        )
