from django.urls import path
from . import views  # views をインポート

app_name = 'bookingfront'

urlpatterns = [
    path('', views.roomselection, name='roomselection'),  # URLを設定
    path('planselection/', views.planselection, name='planselection'),
    path('bookingmanage/', views.bookingmanage, name='bookingmanage'),

    
]
