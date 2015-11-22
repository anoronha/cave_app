from data_collection.models import *
from django.forms import ModelForm

class FieldtripForm(ModelForm):
    class Meta:
        model = Fieldtrip
        fields = ['location', 'beginfieldtrip', 'endfieldtrip', 'note']
        labels = {
            'location': _('Location'),
            'beginfieldtrip': _('Trip Start'),
            'endfieldtrip': _('Trip End'),
            'note': _('Note'),
            }
