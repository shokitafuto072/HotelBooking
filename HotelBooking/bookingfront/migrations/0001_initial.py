# Generated by Django 4.2.6 on 2025-01-28 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('meal_included', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reservation_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth_date')),
                ('postal_number', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=150, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=150, null=True, verbose_name='last_name')),
                ('reservation_date', models.DateField(null=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingfront.plan')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingfront.roomtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
