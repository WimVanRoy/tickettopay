from django.contrib import admin
from nmbs.models import TrainLine, Station, Subscription, Trip, ConfirmedTrip


@admin.register(TrainLine)
class TrainLineAdmin(admin.ModelAdmin):
    list_display = ('train_no', 'train_serv')


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'ticket_type', 'ticket_number',
                    'ticket_last_usage', 'departure_station',
                    'destination_station', 'stop_station')
    ordering = ('-user',)
    list_per_page = 100


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('datdep', 'train_no', 'planned_time_arr',
                    'planned_time_dep', 'delay_arr', 'delay_dep',
                    'ptcar_lg_nm_nl')


@admin.register(ConfirmedTrip)
class ConfirmedTripAdmin(admin.ModelAdmin):
    list_display = ('trip', 'subscription', 'processed')
