from django.db import models

"""
class Reservation(models.Model):
    roomtype=models.CharField("部屋タイプ",max_length=30)
    Reservation_date=models.DateField("予約日付",auto_now=True)
"""

class RoomType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    meal_included = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def create_default_plans(cls):
        # デフォルトプランの登録
        cls.objects.get_or_create(name="シングルプラン", description="シングルルーム1泊", price=5000, meal_included=False)
        cls.objects.get_or_create(name="ダブルプラン", description="ダブルルーム1泊", price=8000, meal_included=False)
        cls.objects.get_or_create(name="スイートプラン", description="スイートルーム1泊", price=15000, meal_included=True)

class Reservation(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    reservation_date = models.DateField()

    def __str__(self):
        return f"Reservation for {self.room_type} on {self.reservation_date}"