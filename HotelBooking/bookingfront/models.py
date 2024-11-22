from django.db import models

class Reservation(models.Model):
    roomtype=models.CharField("部屋タイプ",max_length=30)
    Reservation_date=models.DateField("予約日付",auto_now=True)


# Create your models here.
