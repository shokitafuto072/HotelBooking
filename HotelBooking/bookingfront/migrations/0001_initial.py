# Generated by Django 4.2.6 on 2025-02-06 05:59

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
                ('plan_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('meal_included', models.BooleanField(default=False)),
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
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reservation_date', models.DateField(null=True)),
                ('room_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='RoomAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(blank=True, max_length=50, null=True)),
                ('room_number', models.CharField(blank=True, max_length=10, null=True)),
                ('room_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookingfront.reservation')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingfront.roomtype'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]
