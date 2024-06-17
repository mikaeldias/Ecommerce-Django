from django.urls import path
from .views import *
urlpatterns = [
    path('', homepage, name='homepage'), # nome interno 
    path('loja/', loja, name='loja'), # nome interno 
    path('minhaconta/', minha_conta, name='minha_conta'), # nome interno 
    path('login/', login, name='login'), # nome interno 
    path('carrinho/', carrinho, name='carrinho'), # nome interno 
    path('checkout/', checkout, name='checkout') # nome interno 
]