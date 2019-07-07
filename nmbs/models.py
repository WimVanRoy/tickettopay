from django.db.models import Model, ForeignKey, CharField, FloatField, \
        DateField, DateTimeField, TimeField, BooleanField, SET_NULL, CASCADE
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

TYPE_TICKET = 'ticket'
TYPE_TRAINCARD = 'traincard'
TYPE_CAMPUS = 'campus'
TYPE_HALFTIME = 'halftime'
TYPE_PASS = 'pass'
TYPE_CARD = 'card'
TYPE_MOBIB = 'mobib'
TYPES_OPTIONS = (
    (TYPE_TICKET, _('Ticket')),
    (TYPE_TRAINCARD, _('Train card')),
    (TYPE_CAMPUS, _('Campus')),
    (TYPE_HALFTIME, _('Half-time Train Card')),
    (TYPE_PASS, _('Pass')),
    (TYPE_CARD, _('Card')),
    (TYPE_MOBIB, _('MOBIB-card')),
)


class TrainLine(Model):
    """Train line."""
    train_no = CharField(max_length=10, unique=True)
    train_serv = CharField(max_length=10)


class Station(Model):
    """Train station."""
    name = CharField(max_length=128, unique=True)


class Subscription(Model):
    """Subscription for NMBS."""
    user = ForeignKey(User, null=True, on_delete=SET_NULL,
                      related_name='subscriptions')
    ticket_type = CharField(max_length=30,
                            choices=TYPES_OPTIONS, default=TYPE_MOBIB)
    ticket_number = CharField(max_length=128)
    ticket_last_usage = DateField()

    departure_station = ForeignKey(Station, null=True, on_delete=SET_NULL,
                                  related_name="departures")
    destination_station = ForeignKey(Station, null=True, on_delete=SET_NULL,
                                    related_name="destinations")
    stop_station = ForeignKey(Station, null=True, on_delete=SET_NULL,
                             related_name="stops")


class SubscriptionTrainLines(Model):
    """Linked trainlines to subscriptions."""
    class Meta:
        unique_together = ("subscription", "train")

    subscription = ForeignKey(Subscription, on_delete=CASCADE,
                              related_name='lines')
    train = ForeignKey(TrainLine, on_delete=CASCADE,
                       related_name='links')


class Trips(Model):
    """Train delay."""
    class Meta:
        unique_together = ("datdep", "train_no")

    datdep = DateField()
    recordid = CharField(max_length=64)
    train_no = ForeignKey(TrainLine, related_name='trips', on_delete=CASCADE)

    line_no_arr = CharField(max_length=64)
    line_no_dep = CharField(max_length=64)

    planned_date_arr = DateTimeField()
    planned_time_arr = TimeField()
    planned_date_dep = DateTimeField()
    planned_time_dep = TimeField()

    ptcar_lg_nm_nl = ForeignKey(Station, on_delete=CASCADE)
    real_date_arr = DateField()
    real_date_dep = DateField()
    real_time_arr = TimeField()
    real_time_dep = TimeField()
    relation = CharField(max_length=128)
    relation_direction = CharField(max_length=256)

    real_date_dep = DateField()
    real_date_arr = DateField()
    real_time_dep = TimeField()
    real_time_arr = TimeField()

    train_serv = CharField(max_length=32)
    delay_arr = FloatField()
    delay_dep = FloatField()

    record_timestamp = DateTimeField()


class ConfirmedTrips(Model):
    """Confirmed trips."""
    class Meta:
        unique_together = ("trip", "subscription")

    trip = ForeignKey(Trips, on_delete=CASCADE)
    subscription = ForeignKey(Subscription, related_name='trips',
                             on_delete=CASCADE)
    processed = BooleanField(default=False)
