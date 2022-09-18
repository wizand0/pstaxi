from django.urls import path
from . import views


app_name = 'motorpool'

urlpatterns = [
    path('brand-list/', views.brand_list, name='brand_list'),
    path('brand-detail/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail')
]

