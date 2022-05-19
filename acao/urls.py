from django.urls import path, include
from . import views

app_name = 'acao'
urlpatterns = [
    path('', views.dashboardView.as_view(), name='dashboard'),
    path('doacao', views.doacaoView.as_view(), name='doacao'),
    path('solicitacao', views.solicitacaoView.as_view(), name='solicitacao'),
    path('colaboracao', views.colaboracaoView.as_view(), name='colaboracao'),

]
