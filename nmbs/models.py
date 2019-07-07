from django.db.models import Model, ForeignKey, CharField, FloatField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_laxy as _

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

class TrainNumbers(Model):
    """Train numbers."""
    trainnumber = CharField(max_length=10)

class Subscription(Model):
    """Subscription for NMBS."""
    user = ForeignKey(User, null=True, on_delete=SET_NULL)
    ticket_type = CharField(max_length=30,
                            choices=TYPES_OPTIONS, default=TYPE_MOBIB)
    ticket_number = Charfield(max_length=64)

