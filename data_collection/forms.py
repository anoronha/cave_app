from data_collection.models import *
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.forms import ModelForm, Form, HiddenInput, TextInput, Select, BaseFormSet
import datetime
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.safestring import mark_safe

class NewFieldtripForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (NewFieldtripForm, self).__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.filter(active=1).filter(locationtype='field trip')

    def clean(self):
        cleaned_data = super(NewFieldtripForm, self).clean()
        beginfieldtrip = cleaned_data.get('beginfieldtrip')
        endfieldtrip = cleaned_data.get('endfieldtrip')
        if beginfieldtrip and endfieldtrip:
            if endfieldtrip < beginfieldtrip:
                raise forms.ValidationError(
                "Trip end cannot be before trip start"
                )
    class Meta:
        model = Fieldtrip
        fields = ['location', 'beginfieldtrip', 'endfieldtrip', 'note']
        labels = {
            'location': ('Location'),
            'beginfieldtrip': ('Trip Start'),
            'endfieldtrip': ('Trip End'),
            'note': ('Note'),
            }
        widgets = {
            'beginfieldtrip': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
            'endfieldtrip': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
        }

class SelectteamForm(Form):
    workers = forms.ModelMultipleChoiceField(queryset=Worker.objects.none(),widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        workers = kwargs.pop('workers', Worker.objects.none())
        super (SelectteamForm, self).__init__(*args, **kwargs)
        self.fields['workers'].queryset = workers


class FieldteamForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (FieldteamForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Fieldteam
        fields = ['workername','idfieldtrip']


class WorkerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (WorkerForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Worker
        fields = ['workername', 'workertype','active']
        labels = {
            'workername': ('Other'),
            'workertype': ('Worker Type')
            }
        widgets = {
            'active': HiddenInput(),
            }


class SelectWaterSampleSiteForm(Form):
    selected_sites = forms.ModelMultipleChoiceField(queryset=Site.objects.none(),widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        filtered_sites = kwargs.pop('filtered_sites', Site.objects.none())
        super(SelectWaterSampleSiteForm, self).__init__(*args, **kwargs)
        self.fields['selected_sites'].queryset = filtered_sites
    # def clean(self):
    #     super(SelectWaterSampleSiteForm, self).clean()
    #     if self.cleaned_data.get('selected_sites') in self._errors:
    #         del self._errors['selected_sites']


class SamplenamemasterlistForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (SamplenamemasterlistForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Samplenamemasterlist
        fields = ['samplename','sampletype']


class GroundwatersampledetailsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (GroundwatersampledetailsForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Groundwatersampledetails
        fields = ['samplename','site','idfieldtrip']

class DateTimeSplitForm(Form):
    day = forms.ChoiceField(choices=())
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', None)
        super(DateTimeSplitForm, self).__init__(*args, **kwargs)
        if choices is not None and len(choices)>1:
            self.fields['day'].choices = choices
        else:
            self.fields['day'].widget = HiddenInput()
    time = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(options={"format": "HH:mm"}))


class DripcollectionbottleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DripcollectionbottleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Dripcollectionbottle
        fields = ['samplename','initialmass', 'finalmass', 'deploytime',
                  'collecttime','note']
        labels = {
            'initialmass': ('Intial Bottle Weight'),
            'finalmass': ('Final Bottle Weight'),
            'deploytime': ('Deploy Time'),
            'collecttime': ('Collect Time'),
            'note': ('Note'),
            }
        widgets = {
            'samplename': HiddenInput(),
            'deploytime': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm","defaultDate":"2015-01-01"}),
            'collecttime': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
            }




class DripintervalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        site = kwargs.pop('site', Site.objects.none())
        idfieldtrip = kwargs.pop('idfieldtrip', Fieldtrip.objects.none())
        super(DripintervalForm, self).__init__(*args, **kwargs)
        self.fields['site'].queryset = Site.objects.filter(site = site)
        self.fields['idfieldtrip'].queryset = Fieldtrip.objects.filter(idfieldtrip = idfieldtrip)
    class Meta:
        model = Dripinterval
        fields = ['site','idfieldtrip','timecollected','count1', 'count2', 'count3']
        labels = {
            'timecollected': ('Time Drip Count Measured'),
            'count1': ('Drip Count Measurement 1'),
            'count2': ('Drip Count Measurement 2'),
            'count3': ('Drip Count Measurement 3'),
            }
        widgets = {
            'site': HiddenInput(),
            'idfieldtrip': HiddenInput(),
            'timecollected': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"})
            }

class PlatecollectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        idfieldtrip = kwargs.pop('idfieldtrip', Fieldtrip.objects.none())
        super(PlatecollectForm, self).__init__(*args, **kwargs)
        self.fields['collectfieldtrip'].queryset = Fieldtrip.objects.filter(idfieldtrip = idfieldtrip)
    class Meta:
        model = Platefielddata
        fields = ['samplename','datedeploy','datecollect','collectfieldtrip']
        labels = {
            'samplename': ('Collected Plate Name'),
            'datedeploy': ('Date Deployed'),
            'datecollect': ('Date Plate Collected'),
            }
        widgets = {
            'samplename': TextInput(attrs={'readonly':'readonly'}),
            'datedeploy': TextInput(attrs={'readonly':'readonly'}),
            'collectfieldtrip': HiddenInput(),
            'datecollect': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
            }

class PlatedeplyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        site = kwargs.pop('site', Site.objects.none())
        idfieldtrip = kwargs.pop('idfieldtrip', Fieldtrip.objects.none())
        super(PlatedeplyForm, self).__init__(*args, **kwargs)
        self.fields['site'].queryset = Site.objects.filter(site = site)
        self.fields['deployfieldtrip'].queryset = Fieldtrip.objects.filter(idfieldtrip = idfieldtrip)
        self.fields['samplename'].queryset = Samplenamemasterlist.objects.filter(sampletype='glass plate').order_by('-idsamplenamemasterlist')
    class Meta:
        model = Platefielddata
        fields = ['site','samplename','datedeploy','deployfieldtrip']
        labels = {
            'samplename': ('Deployed Plate Name'),
            'datedeploy': ('Time Plate Deployed'),
            }
        widgets = {
            'site': HiddenInput(),
            'deployfieldtrip': HiddenInput(),
            'datedeploy': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
            }

class FieldwaterchemistryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        samplename = kwargs.pop('samplename', Site.objects.none())
        super(FieldwaterchemistryForm, self).__init__(*args, **kwargs)
        self.fields['samplename'].queryset = Samplenamemasterlist.objects.filter(samplename = samplename)
        #add an active/inactive field to the fieldinstruement name
        self.fields['fieldinstrumentname'].queryset = Fieldinstrumentname.objects.filter(fieldinstrumenttype='Ultrameter')
    class Meta:
        model = Fieldwaterchemistry
        fields = ['samplename','fieldinstrumentname','orp','tds','conductivity','ph','temp']
        labels = {
            'fieldinstrumentname': ('Ultrameter name'),
            'orp': ('ORP'),
            'tds': ('TDS'),
            'conductivity': ('Conductivity'),
            'ph': ('pH'),
            'temp': ('Temperature')
            }
        widgets = {
            'samplename': HiddenInput(),
            }


class AlkalinityForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (AlkalinityForm, self).__init__(*args, **kwargs)
        self.fields['samplename'].queryset = Samplenamemasterlist.objects.filter(sampletype='groundwater').order_by('-idsamplenamemasterlist')[:20]
        self.fields['workername'].queryset = Worker.objects.filter(active=1).filter(workertype='General')
    class Meta:
        model = Alkalinity
        fields = ['samplename','dateanalyzed', 'cartrige', 'volume',
                  'starttemp','endtemp','startph','endph','alkdigit',
                  'alkalinity','workername']
        labels = {
            'samplename': ('Sample Name'),
            'cartrige': ('Acid Cartrige Number'),
            'dateanalyzed': ('Date Analyzed'),
            'volume': ('Sample Volume'),
            'starttemp': ('Starting Water Temp'),
            'endtemp': ('Ending Water Temp'),
            'startph': ('Starting Water pH'),
            'endph': ('Ending Water pH'),
            'alkdigit': ('Alk Digit'),
            'alkalinity': ('Calculated Alkalinity'),
            'workername': ('Measured By'),
            }
        widgets = {
            'dateanalyzed': DateTimePicker(options={"format": "YYYY-MM-DD"})}

class WatersampleinventoryForm (ModelForm):
    # fillamount = forms.ChoiceField(choices=[0.0,1.0])
    def __init__(self, *args, **kwargs):
        samplename = kwargs.pop('samplename', Site.objects.none())
        super (WatersampleinventoryForm, self).__init__(*args, **kwargs)
        self.fields['samplename'].queryset = Samplenamemasterlist.objects.filter(samplename = samplename)
    class Meta:
        model = Watersampleinventory
        fields = ['samplename','bottlesize', 'bottletype', 'preservative',
                  'intendedanalysis','fillamount']
                  #add fill amount once I've recompiled the database
        labels = {
            'samplename': ('Sample Name'),
            'bottlesize': ('Bottle Size'),
            'bottletype': ('Bottle Type'),
            'preservative': ('Preservative'),
            'intendedanalysis': ('Intented Analysis'),
            'fillamount': ('Fill level'),
            }
        widgets = {
            'samplename': HiddenInput(),
            'intendedanalysis': HiddenInput(),
            'fillamount': Select(choices=((None, '--------'),
                                         ('0.25','less than half'),
                                         ('0.5','half'),
                                         ('0.75','more than half'),
                                         ('1.0','full')))

            }

class Fieldco2SpotForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (Fieldco2SpotForm, self).__init__(*args, **kwargs)
        self.fields['fieldinstrumentname'].queryset = Fieldinstrumentname.objects.filter(fieldinstrumenttype='CO2 Logger')
    class Meta:
        model = Fieldco2Spot
        fields = ['site','fieldinstrumentname', 'datetime', 'co2']
        labels = {
            'site': ('Site'),
            'fieldinstrumentname': ('Logger Name'),
            'datetime': ('Measurement Time'),
            'co2': mark_safe(u'CO<sub>2</sub>'),
            }

class BaseFieldco2SpotFormset(BaseFormSet):
    def add_fields(self, form, index):
        super(BaseFieldco2SpotFormset, self).add_fields(form, index)
        form.fields['fieldinstrumentname'].queryset = Fieldinstrumentname.objects.filter(fieldinstrumenttype='CO2 Logger')

class UploadFileForm(Form):
    file = forms.FileField()
