from django.db import models
from django.contrib.auth import get_user_model 

User=get_user_model()

"""
class Reservation(models.Model):
    roomtype=models.CharField("部屋タイプ",max_length=30)
    Reservation_date=models.DateField("予約日付",auto_now=True)
"""

class RoomType(models.Model):
    name = models.CharField(max_length=50)
    reservation_date=models.DateField(null=True)
    room_price = models.DecimalField(max_digits=8, decimal_places=2,null=False)
    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plan_price = models.DecimalField(max_digits=8, decimal_places=2)
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
    PAYMENT_METHOD_CHOICES = [
        ('現金', '現金'),
        ('クレジットカード', 'クレジットカード'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reservations")
    password = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name=("email"),
        unique=True
    )
    birth_date = models.DateField(
        verbose_name=("birth_date"),
        blank=True,
        null=True
    )
    postal_number=models.CharField(max_length=7)
    address=models.CharField(max_length=100)
    first_name = models.CharField(
        verbose_name=("first_name"),
        max_length=150,
        null=True,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=("last_name"),
        max_length=150,
        null=True,
        blank=False
    )
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    reservation_date=models.DateField(null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
   

    def __str__(self):
        return f"Reservation for {self.user.account_id} in {self.room_type.name} on {self.reservation_date}"
    
    def save(self, *args, **kwargs):
        if self.user:
            # ユーザーの情報をReservationにコピー
            self.account_id = self.user.account_id
            self.password = self.user.password
            self.email = self.user.email
            self.birth_date = self.user.birth_date
            self.postal_number = self.user.postal_number
            self.address = self.user.address
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name

        if self.room_type:
            # ユーザーの情報をReservationにコピー
           self.reservation_date = self.room_type.reservation_date
        super(Reservation, self).save(*args, **kwargs)

class RoomAllocation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True)  # null=True, blank=True で任意に設定
    room_type = models.CharField(max_length=50, null=True, blank=True)  # null=True, blank=True で任意
    room_number = models.CharField(max_length=10, null=True, blank=True)  # null=True, blank=True で任意
    room_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # null=True, blank=True で任意
    description = models.TextField(null=True, blank=True)  # null=True, blank=True で任意
    first_name = models.CharField(max_length=150, null=True, blank=True)  # first_name は任意に設定
    last_name = models.CharField(max_length=150, null=True, blank=True)  # last_name は任意に設定

    def __str__(self):
        return f"{self.room_number} ({self.room_type})"
    
    # save メソッドをカスタマイズして、必要な情報を予約情報から引き継げるようにする
    def save(self, *args, **kwargs):
        if self.reservation:
            self.first_name = self.reservation.first_name
            self.last_name = self.reservation.last_name
            self.room_type = self.reservation.room_type.name  # 予約の部屋タイプを使用

        super(RoomAllocation, self).save(*args, **kwargs)

    
 
    
