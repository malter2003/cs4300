# Generated by Django 5.1.6 on 2025-03-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_remove_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('movie', 'seat_number')},
        ),
    ]
