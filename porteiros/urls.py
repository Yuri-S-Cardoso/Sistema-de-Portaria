from django.urls import path
from . import views


urlpatterns = [

    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro_inter/', views.cadastro_inter, name='cadastro_inter'),
    path('cadastro_terceiros/', views.cadastro_terceiros, name='cadastro_terceiros'),
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastro_veiculo/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('cadastro_motorista/', views.cadastro_motorista, name='cadastro_motorista'),
    path('cadastro_inter_entrada/', views.cadastro_inter_entrada, name='cadastro_inter_entrada'),
    path('verificar_entrada/', views.verificar_entrada, name='verificar_entrada'),
    path('buscar_veiculo/', views.buscar_veiculo, name='buscar_veiculo'),
    path('cadastro_cnpj_terceiros/', views.cadastro_cnpj_terceiros, name='cadastro_cnpj_terceiros'),
    path('verificar_cnpj/', views.verificar_cnpj, name='verificar_cnpj'),
    path('verificar_placa/', views.verificar_placa, name='verificar_placa'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('relatorio_inter_saida/', views.relatorio_inter_saida, name='relatorio_inter_saida'),
    path('relatorio_inter_entrada/', views.relatorio_inter_entrada, name='relatorio_inter_entrada'),
    path('relatorio_terceiros_saida/', views.relatorio_terceiros_saida, name='relatorio_terceiros_saida'),
    path('relatorio_terceiros_entrada/', views.relatorio_terceiros_entrada, name='relatorio_terceiros_entrada'),
    path('cadastro_terceiros_saida/', views.cadastro_terceiros_saida, name='cadastro_terceiros_saida'),
    path('busca_terceiros/', views.busca_terceiros, name='busca_terceiros'),
    path('cupom/', views.cupom, name='cupom'),
]
