from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre producto")
    price = models.FloatField(verbose_name="Precio", default=0)
    stock = models.IntegerField(verbose_name="Stock", default=0)
    image = models.CharField(null=True, blank=True, verbose_name="URL imagen de producto")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product)
    name_buyer = models.CharField(max_length=70, verbose_name="Nombre del comprador")

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes de compra"

    def __str__(self):
        return f"Orden {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="Cantidad", default=0)

    class Meta:
        verbose_name = "Orden de compra"
        verbose_name_plural = "Ordenes de compra"

    def __str__(self):
        return f"{self.order.name_buyer} compró {self.quantity}x {self.product.name}"

class DiscountCode(models.Model):
    code = models.CharField(max_length=50, verbose_name="Nombre producto")
    discount = models.FloatField(verbose_name="Descuento", default=0)
    quantity = models.IntegerField(verbose_name="Cantidad de veces que se puede usar", default=0)

    class Meta:
        verbose_name = "Código de descuento"
        verbose_name_plural = "Códigos de descuento"

    def __str__(self):
        return self.code + ' ' + str(self.discount) + ' ' + str(self.quantity)


class WelcomeMessage(models.Model):
    message = models.CharField(max_length=100, verbose_name="Mensaje de bienvenida")
    temperature_min = models.IntegerField(verbose_name="Temperatura mínima (mínima 0°)")
    temperature_max = models.IntegerField(verbose_name="Temperatura máxima (máxima 50°)")

    class Meta:
        verbose_name = "Mensaje de bienvenida"
        verbose_name_plural = "Mensajes de bienvenida"

    def __str__(self):
        return self.message

    def clean(self):
        if self.temperature_min < 0:
            raise ValidationError("La temperatura mínima debe ser mayor a 0.")

        if self.temperature_max > 50:
            raise ValidationError("La temperatura máxima debe ser menor a 50.")

        if self.temperature_min >= self.temperature_max:
            raise ValidationError("La temperatura mínima debe ser menor que la temperatura máxima.")

        '''
        Verificar superposición con otros mensajes existentes
        1. Existe algún mensaje en el que su temperatura mínima esté entre el rango de temperaturas del mensaje actual.
        2. Existe algún mensaje en el que su temperatura máxima esté entre el rango de temperaturas del mensaje actual.
        3. Existe algún mensaje en el que su rango de temperaturas incluya completamente el rango de temperaturas del mensaje actual.
        '''
        if WelcomeMessage.objects.filter(
                ~Q(id=self.id),
                (Q(temperature_min__gte=self.temperature_min, temperature_min__lt=self.temperature_max) |
                 Q(temperature_max__gt=self.temperature_min, temperature_max__lte=self.temperature_max)) |
                (Q(temperature_min__lte=self.temperature_min, temperature_max__gt=self.temperature_max) &
                 ~(Q(temperature_min=self.temperature_min) & Q(temperature_max=self.temperature_max)))
        ).exists():
            raise ValidationError("El rango de temperaturas se superpone con otro mensaje existente.")
