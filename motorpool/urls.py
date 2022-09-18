from django.urls import path
from . import views


app_name = 'motorpool'

urlpatterns = [
    path('brand-list/', views.BrandListView.as_view(), name='brand_list'),
    path('brand-detail/<int:pk>/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('send-email/', views.send_email_view, name='send_email'),
]

