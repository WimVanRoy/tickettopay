# Generated by Django 2.2.3 on 2019-07-07 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nmbs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConfirmedTrips',
            new_name='ConfirmedTrip',
        ),
        migrations.RenameModel(
            old_name='SubscriptionTrainLines',
            new_name='SubscriptionTrainLine',
        ),
        migrations.RenameModel(
            old_name='Trips',
            new_name='Trip',
        ),
    ]