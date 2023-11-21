from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.all_users_endpoint),
    path('<str:user_id>/', views.specific_recycle_endpoint)
]