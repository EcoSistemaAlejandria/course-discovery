from django.utils.translation import gettext_lazy as _
from djchoices import ChoiceItem, DjangoChoices


class PathwayStatus(DjangoChoices):
    Active = ChoiceItem('active', _('Active'))
    Inactive = ChoiceItem('inactive', _('Inactive'))
