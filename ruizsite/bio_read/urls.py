from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_text, name='input_text'),  # 输入页面
    path('result/', views.show_bionic_text, name='show_bionic_text'),
]
