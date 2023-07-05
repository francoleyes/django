from rest_framework import serializers
from ..models import WelcomeMessage, Product, DiscountCode, Order, OrderItem

class WelcomeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeMessage
        fields = ['message']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    products = OrderItemSerializer(many=True)
    total = serializers.FloatField(default=0)

    class Meta:
        model = Order
        fields = ('products', 'name_buyer', 'total')

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        total = validated_data.pop('total')
        order = Order.objects.create(total=total, **validated_data)

        for product_data in products_data:
            OrderItem.objects.create(order=order, **product_data)

        return order
