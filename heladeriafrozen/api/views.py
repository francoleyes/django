from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from ..utils import GeoAPI, validate_discount_code
from ..models import WelcomeMessage, Product, DiscountCode, OrderItem
from .serializers import WelcomeMessageSerializer, ProductSerializer, DiscountCodeSerializer, OrderSerializer

class WelcomeMessageAPIView(APIView):
    def get(self, request):
        temperature = float(GeoAPI.is_hot_in_pehuajo())
        if temperature:
            welcome_message = WelcomeMessage.objects.filter(
                temperature_min__lte=temperature,
                temperature_max__gte=temperature
            ).first()

            if welcome_message:
                serializer = WelcomeMessageSerializer(welcome_message)
                return Response(serializer.data)

        return Response({"message": "Bienvenida por defecto."})

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ValidateDiscountCodeAPIView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        discount_codes = DiscountCode.objects.all()
        validated_code = validate_discount_code(code, discount_codes)

        if validated_code:
            if validated_code.quantity > 0:
                serializer = DiscountCodeSerializer(validated_code)
                return Response(serializer.data)
            else:
                return Response({'error': 'El código de descuento ha alcanzado su límite de uso.'})

        else:
            return Response({'error': 'Código de descuento inválido.'})

class OrderCreateAPIView(APIView):
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            products_data = serializer.validated_data['products']
            discount_code = serializer.validated_data.get('discount_code')

            errors = []
            for product_data in products_data:
                product = product_data['product']
                quantity = product_data['quantity']

                if product.stock < quantity:
                    error_message = f"No hay suficiente stock para el producto {product.name}."
                    errors.append(error_message)

            if errors:
                return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

            for product_data in products_data:
                product = product_data['product']
                quantity = product_data['quantity']
                product.stock -= quantity
                product.save()

            if discount_code is not None:
                if discount_code.quantity <= 0:
                    error_message = "El código de descuento ya no está disponible."
                    return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

                discount_code.quantity -= 1
                discount_code.save()

            order = serializer.save()

            return Response({'message': 'Orden de compra creada correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
