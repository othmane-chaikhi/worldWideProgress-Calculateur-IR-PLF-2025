from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/<int:calculation_id>/', views.result, name='result'),
    path('history/', views.history, name='history'),
    path('export/excel/<int:calculation_id>/', views.export_excel, name='export_excel'),
    path('export/pdf/<int:calculation_id>/', views.export_pdf, name='export_pdf'),
]