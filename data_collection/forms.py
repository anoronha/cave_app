from data_collection.models import *
from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.forms import ModelForm, Form, HiddenInput, TextInput, Select, BaseFormSet
import datetime
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

YES_NO = [(True, "Yes"), (False, "No")]

class NewFieldtripForm(Form):
    location = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'select form-control'}), queryset=Location.objects.none(),label='Location')
    beginfieldtrip = forms.ChoiceField(widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
                                       label='Trip Start')
    endfieldtrip = forms.ChoiceField(widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}),
                                     label='Trip End')
    workers = forms.ModelMultipleChoiceField(queryset=Worker.objects.none(),
                                             widget=forms.CheckboxSelectMultiple,
                                             label='Field Team',
                                             required=False)
    note = forms.CharField(label='Note',
                           required=False,
                           widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        workers = kwargs.pop('workers', Worker.objects.none())
        super(NewFieldtripForm, self).__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.filter(active=1).filter(locationtype='field trip')
        self.fields['workers'].queryset = workers
    def clean(self):
        cleaned_data = super(NewFieldtripForm, self).clean()
        beginfieldtrip = cleaned_data.get('beginfieldtrip')
        endfieldtrip = cleaned_data.get('endfieldtrip')
        if beginfieldtrip and endfieldtrip:
            if endfieldtrip < beginfieldtrip:
                raise forms.ValidationError(
                "You can't start a trip before you end it!"
                )


class WorkerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super (WorkerForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Worker
        fields = ['idworker','workername','workertype','affiliation','jobtitle','active','email','phonenumber']
        labels = {
            'workername': ('Name'),
            'workertype': ('Work type'),
            'affiliation': ('Primary affiliation'),
            'jobtitle': ('Job Title'),
            'active': ('Currently active'),
            'email': ('E-mail'),
            'phonenumber': ('Phone number'),
            }
        widgets = {
            'active': Select(choices=YES_NO),
            'idworker': TextInput(attrs={'readonly':'readonly'}),
            }

class ExistingWorkerForm(Form):
    existing_workers = forms.ModelChoiceField(queryset=Worker.objects.all(),label='Modify existing profile')
    def __init__(self, *args, **kwargs):
        super (ExistingWorkerForm, self).__init__(*args, **kwargs)


class SitesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super (SitesForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Site
        fields = ['site','location','sitetype','xlocation','ylocation','sitecode','note','active']
        labels = {
            'site': ('Site Name'),
            'location': ('Location'),
            'sitetype': ('Site type'),
            'xlocation': ('Easting (UTM Zone 55N)'),
            'ylocation': ('Northing (UTM Zone 55N)'),
            'sitecode': ('Site Code (3-5 letters all caps)'),
            'note': ('Note'),
            'active': ('Currently Active')
            }


class SelectWaterSampleSiteForm(Form):
    selected_sites = forms.ModelMultipleChoiceField(queryset=Site.objects.none(),widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        filtered_sites = kwargs.pop('filtered_sites', Site.objects.none())
        super(SelectWaterSampleSiteForm, self).__init__(*args, **kwargs)
        self.fields['selected_sites'].queryset = filtered_sites


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

class CavedripwaterForm(Form):
    bottle_down_day = forms.ChoiceField(choices=())
    bottle_down_time = forms.DateTimeField(required=False, widget=DateTimePicker(options={"format": "HH:mm"}, icon_attrs={'class': 'glyphicon glyphicon-time'}),label = 'Time')
    initialmass = forms.DecimalField(label='Initial Mass')
    bottle_up_day = forms.ChoiceField(choices=())
    bottle_up_time = forms.DateTimeField(required=False, widget=DateTimePicker(options={"format": "HH:mm"}, icon_attrs={'class': 'glyphicon glyphicon-time'}), label = 'Time')
    finalmass = forms.DecimalField(label='Final Mass')
    watersamplename = forms.CharField(widget=HiddenInput())
    dripcount_day = forms.ChoiceField(choices=())
    dripcount_time = forms.DateTimeField(required=False, widget=DateTimePicker(options={"format": "HH:mm"}, icon_attrs={'class': 'glyphicon glyphicon-time'}),label = 'Time')
    dripcount_1 = forms.IntegerField(label='Drip Count 1')
    dripcount_2 = forms.IntegerField(label='Drip Count 2')
    dripcount_3 = forms.IntegerField(label='Drip Count 3')
    fieldinstrumentname = forms.ModelChoiceField(queryset=())
    orp = forms.DecimalField(label='ORP')
    tds = forms.DecimalField(label='TDS')
    conductivity = forms.DecimalField(label='TDS')
    ph = forms.DecimalField(label='pH')
    temp = forms.DecimalField(label='Temperature')
    def __init__(self, *args, **kwargs):
        day_choices = kwargs.pop('day_choices', None)
        flag = kwargs.pop('trip_length_flag', None)
        initialmass = kwargs.pop('initialmass', None)
        watersamplename = kwargs.pop('watersamplename', None)
        super(CavedripwaterForm, self).__init__(*args, **kwargs)
        self.fields['fieldinstrumentname'].queryset = Fieldinstrumentname.objects.filter(fieldinstrumenttype='Ultrameter')
        if day_choices is not None and flag == 0:
            self.fields['bottle_down_day'].choices = day_choices
            self.fields['bottle_up_day'].choices = day_choices
            self.fields['dripcount_day'].choices = day_choices
        elif day_choices is not None:
            self.fields['bottle_down_day'].choices = day_choices
            self.fields['bottle_up_day'].choices = day_choices
            self.fields['bottle_down_day'].widget = HiddenInput()
            self.fields['bottle_up_day'].widget = HiddenInput()
        if initialmass is not None:
            self.fields['initialmass'].initial = initialmass
        if watersamplename is not None:
            # self.fields['watersamplename'].queryset = Samplenamemasterlist.objects.filter(samplename=watersamplename)
            self.fields['watersamplename'].initial = watersamplename
    note = forms.CharField(label='Note')

class DripcollectionbottleSubmitForm(ModelForm):
    class Meta:
        model = Dripcollectionbottle
        fields = ['samplename','initialmass', 'finalmass', 'deploytime',
                  'collecttime','note']


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
