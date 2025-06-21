from django.urls import path
from . import views

urlpatterns = [
    path('public/', views.public_api, name='public'),
    path('protected/', views.protected_api, name='protected'),
]
