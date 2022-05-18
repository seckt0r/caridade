from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboardView.as_view(), name='dashboard'),
    path('colaboradores', views.colaboradoresView.as_view(), name='colaboradores'),

]
