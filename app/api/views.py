from django.db.models import F, Prefetch, Min, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import views
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app.api import serializer
from rest_framework.response import Response

from app.api.serializer import ProductSerializer
from app.models import Product, Price, Size


class ProductView(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('sku',)

    def list(self, request, *args, **kwargs):
        products = super().get_queryset().annotate(
            min_price=Min('size__price_size__price'),
            brand_name=F('brand__title')
        ).prefetch_related(
            Prefetch(
                'size',
                Size.objects.annotate(
                    price=F('price_size__price')
                ).exclude(
                    price=None,
                ).order_by(
                    'price',
                )
            )
        )

        if not products:
            return Response('Error')
        return Response(ProductSerializer(instance=products, many=True).data)
