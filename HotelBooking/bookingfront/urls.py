from django.urls import path
from . import views  # views をインポート

urlpatterns = [
    path('', views.roomselection, name='roomselection'),  # URLを設定
]
