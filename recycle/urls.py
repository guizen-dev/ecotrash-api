from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.all_recycling_endpoint),
    path('<str:recycle_id>/', views.specific_user_endpoint)
]