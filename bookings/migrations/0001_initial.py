# Generated by Django 3.2.20 on 2023-07-31 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_seats', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('requested_date', models.DateField()),
                ('requested_time', models.CharField(choices=[('12:00', '12:00 PM'), ('13:15', '1:15 PM'), ('14:30', '2:30 PM'), ('15:45', '3:45 PM'), ('17:00', '5:00 PM'), ('18:15', '6:15 PM'), ('19:30', '7:30 PM'), ('20:45', '8:45 PM'), ('22:00', '10:00 PM'), ('23:15', '11:15 PM')], default='12:00', max_length=5)),
                ('seats', models.IntegerField()),
                ('guest_count', models.IntegerField()),
                ('status', models.CharField(choices=[('PN', 'Pending'), ('CF', 'Confirmed'), ('CM', 'Completed'), ('CL', 'Cancelled')], default='PN', max_length=2)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.restauranttable')),
            ],
        ),
    ]