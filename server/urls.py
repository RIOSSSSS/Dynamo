# urls.py
from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.urls import path
from . import views  # Ajuste este import para o local onde sua view de login está definida
from .views import home
from .views import MeusDadosView
from .views import webhook, sucesso, falha
from django.urls import path, include
from .views import enderecos_cadastrados
from .views import meus_pedidos
from .views import custom_logout
from .views import atualizar_informacoes
from .views import favoritos
from .views import minhas_compras



  # Importe suas views aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('menu/', views.menu_views, name='menu'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),  # Adicione esta linha para a rota de cadastro
    path('item1/', views.item1_view, name='item1'), 
    path('item2/', views.item2_view, name='item2'),
    path('item3/', views.item3_view, name='item3'),
    path('item4/', views.item4_view, name='item4'),
    path('item5/', views.item5_view, name='item5'), 
    path('novo1/', views.novo1_view, name='novo1'), 
    path('novo2/', views.novo2_view, name='novo2'),
    path('novo3/', views.novo3_view, name='novo3'),
    path('novo4/', views.novo4_view, name='novo4'),
    path('novo5/', views.novo5_view, name='novo5'), 
    path('meus_dados/', MeusDadosView.as_view(), name='meus_dados'),
    path('webhook/', webhook, name='webhook'),
    path('sucesso/', sucesso, name='url_sucesso'),
    path('falha/', falha, name='url_falha'),
    path('admin/', admin.site.urls),
    path('logout/', custom_logout, name='logout'),
    path('enderecos_cadastrados/', enderecos_cadastrados, name='enderecos_cadastrados'),
    path('favoritos/', favoritos, name='favoritos'),
    path('meus_pedidos/', meus_pedidos, name='meus_pedidos'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('minhas-compras/', minhas_compras, name='minhas_compras'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('seu-novo-endpoint/', atualizar_informacoes, name='atualizar_informacoes'),
    
    
    
    
]






