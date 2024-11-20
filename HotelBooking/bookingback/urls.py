from django.urls import path
from . import views  # views をインポート


urlpatterns = [
    path('',views.dashboard,name="dashboard"),
]
