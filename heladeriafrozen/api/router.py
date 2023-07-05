from django.urls import path

from heladeriafrozen.api.views import WelcomeMessageAPIView, ProductAPIView, ValidateDiscountCodeAPIView, OrderCreateAPIView

urlpatterns = [
    path('welcome-message/', WelcomeMessageAPIView.as_view()),
    path('products/', ProductAPIView.as_view()),
    path('discount/validate/', ValidateDiscountCodeAPIView.as_view()),
    path('create-order/', OrderCreateAPIView.as_view()),
]