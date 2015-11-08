# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Alkalinity(models.Model):
    idalkalinity = models.IntegerField(db_column='idAlkalinity', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    dateanalyzed = models.DateTimeField(db_column='DateAnalyzed', blank=True, null=True)  # Field name made lowercase.
    cartrige = models.IntegerField(db_column='Cartrige', blank=True, null=True)  # Field name made lowercase.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    starttemp = models.TextField(db_column='StartTemp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startph = models.TextField(db_column='StartpH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endtemp = models.TextField(db_column='EndTemp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endph = models.TextField(db_column='EndpH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    alkdigit = models.TextField(db_column='AlkDigit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    alkalinity = models.TextField(db_column='Alkalinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    worker = models.TextField(db_column='Worker', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alkalinity'


class Analysis(models.Model):
    idanalysis = models.IntegerField(db_column='idAnalysis', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    analysis = models.TextField(db_column='Analysis', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Analysis'


class Analyte(models.Model):
    idanalyte = models.IntegerField(db_column='idAnalyte', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    analyte = models.TextField(db_column='Analyte', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Analyte'


class Anionresults(models.Model):
    idanionresults = models.IntegerField(db_column='idAnionResults', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.TextField(db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.TextField(db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    f = models.TextField(db_column='F', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cl = models.TextField(db_column='Cl', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    no2 = models.TextField(db_column='NO2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    so4 = models.TextField(db_column='SO4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    br = models.TextField(db_column='Br', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    no3 = models.TextField(db_column='NO3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    po4 = models.TextField(db_column='PO4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.TextField(db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnionResults'


class Bottlesize(models.Model):
    idbottlesize = models.IntegerField(db_column='idBottleSize', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    bottlesize = models.TextField(db_column='BottleSize', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BottleSize'


class Bottletype(models.Model):
    idbottletype = models.IntegerField(db_column='idBottleType', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    bottletype = models.TextField(db_column='BottleType', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BottleType'


class Cationresults(models.Model):
    idcationresults = models.IntegerField(db_column='idCationResults', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.TextField(db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.TextField(db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    li = models.TextField(db_column='Li', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ag = models.TextField(db_column='Ag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    al = models.TextField(db_column='Al', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    as_field = models.TextField(db_column='As', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word. This field type is a guess.
    b = models.TextField(db_column='B', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ba = models.TextField(db_column='Ba', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    be = models.TextField(db_column='Be', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bi = models.TextField(db_column='Bi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ca = models.TextField(db_column='Ca', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cd = models.TextField(db_column='Cd', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    co = models.TextField(db_column='Co', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cr = models.TextField(db_column='Cr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cs = models.TextField(db_column='Cs', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cu = models.TextField(db_column='Cu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe = models.TextField(db_column='Fe', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ge = models.TextField(db_column='Ge', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    k = models.TextField(db_column='K', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lu = models.TextField(db_column='Lu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mg = models.TextField(db_column='Mg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mn = models.TextField(db_column='Mn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mo = models.TextField(db_column='Mo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    na = models.TextField(db_column='Na', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ni = models.TextField(db_column='Ni', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p = models.TextField(db_column='P', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pb = models.TextField(db_column='Pb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rb = models.TextField(db_column='Rb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    s = models.TextField(db_column='S', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sb = models.TextField(db_column='Sb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sc = models.TextField(db_column='Sc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    se = models.TextField(db_column='Se', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    si = models.TextField(db_column='Si', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sn = models.TextField(db_column='Sn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sr = models.TextField(db_column='Sr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    te = models.TextField(db_column='Te', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    th = models.TextField(db_column='Th', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ti = models.TextField(db_column='Ti', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tl = models.TextField(db_column='Tl', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    u = models.TextField(db_column='U', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    v = models.TextField(db_column='V', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zn = models.TextField(db_column='Zn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zr = models.TextField(db_column='Zr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.TextField(db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CationResults'


class Dripcollectionbottle(models.Model):
    iddripcollectionbottle = models.IntegerField(db_column='idDripCollectionBottle', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    initialmass = models.TextField(db_column='InitialMass', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finalmass = models.TextField(db_column='FinalMass', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deploytime = models.DateTimeField(db_column='DeployTime', blank=True, null=True)  # Field name made lowercase.
    collecttime = models.DateTimeField(db_column='CollectTime', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DripCollectionBottle'


class Dripinterval(models.Model):
    iddripinterval = models.IntegerField(db_column='idDripInterval', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idfieldtrip = models.IntegerField(db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    timecollected = models.DateTimeField(db_column='TimeCollected', blank=True, null=True)  # Field name made lowercase.
    count1 = models.IntegerField(db_column='Count1', blank=True, null=True)  # Field name made lowercase.
    count2 = models.IntegerField(db_column='Count2', blank=True, null=True)  # Field name made lowercase.
    count3 = models.IntegerField(db_column='Count3', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DripInterval'


class Dripperminute(models.Model):
    iddripperminute = models.IntegerField(db_column='idDripPerMinute', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idfieldtrip = models.IntegerField(db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    timecollected = models.DateTimeField(db_column='TimeCollected', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    minutes = models.IntegerField(db_column='Minutes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DripPerMinute'


class Fieldco2(models.Model):
    idfieldco2 = models.IntegerField(db_column='idFieldCO2', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.TextField(db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    lognumber = models.IntegerField(db_column='LogNumber', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    co2 = models.IntegerField(db_column='CO2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldCO2'


class Fieldinstruementservicerecord(models.Model):
    idfieldinstruementservicerecord = models.IntegerField(db_column='idFieldInstruementServiceRecord', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.TextField(db_column='FieldInstrumentName')  # Field name made lowercase.
    dateshippedout = models.TextField(db_column='DateShippedOut')  # Field name made lowercase.
    datereturned = models.TextField(db_column='DateReturned', blank=True, null=True)  # Field name made lowercase.
    servicerecord = models.TextField(db_column='ServiceRecord', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstruementServiceRecord'


class Fieldinstrumentcomponent(models.Model):
    idfieldinstrumentcomponent = models.IntegerField(db_column='idFieldInstrumentComponent', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=45, blank=True, null=True)  # Field name made lowercase.
    partnumber = models.TextField(db_column='PartNumber', blank=True, null=True)  # Field name made lowercase.
    partname = models.TextField(db_column='PartName', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    datepurchased = models.DateTimeField(db_column='DatePurchased', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentComponent'


class Fieldinstrumentdetails(models.Model):
    idfieldinstrumentdetails = models.IntegerField(db_column='idFieldInstrumentDetails', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.TextField(db_column='FieldInstrumentName')  # Field name made lowercase.
    fieldinstrumentcomponent = models.TextField(db_column='FieldInstrumentComponent', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.DateTimeField(db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentDetails'


class Fieldinstrumentname(models.Model):
    idfieldinstrumentname = models.IntegerField(db_column='idFieldInstrumentName', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.TextField(db_column='FieldInstrumentName', unique=True)  # Field name made lowercase.
    fieldinstrumenttype = models.TextField(db_column='FieldInstrumentType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentName'


class Fieldinstrumenttype(models.Model):
    idfieldinstrumenttype = models.IntegerField(db_column='idFieldInstrumentType', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    fieldinstrumenttype = models.TextField(db_column='FieldInstrumentType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentType'


class Fieldtrip(models.Model):
    idfieldtrip = models.IntegerField(db_column='idFieldTrip', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    beginfieldtrip = models.DateTimeField(db_column='BeginFieldTrip', blank=True, null=True)  # Field name made lowercase.
    endfieldtrip = models.DateTimeField(db_column='EndFieldTrip', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldTrip'


class Fieldwaterchemistry(models.Model):
    idfieldwaterchemistry = models.IntegerField(db_column='idFieldWaterChemistry', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.TextField(db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    orp = models.TextField(db_column='ORP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tds = models.TextField(db_column='TDS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conductivity = models.TextField(db_column='Conductivity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ph = models.TextField(db_column='pH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp = models.TextField(db_column='Temp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    salinity = models.TextField(db_column='Salinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldWaterChemistry'


class Fieldweatherstationdata(models.Model):
    idfieldweatherstationdata = models.IntegerField(db_column='idFieldWeatherStationData', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.TextField(db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    lognumber = models.IntegerField(db_column='LogNumber', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    temp = models.TextField(db_column='Temp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rh = models.TextField(db_column='RH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pressure = models.TextField(db_column='Pressure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lightintensity = models.TextField(db_column='LightIntensity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldWeatherStationData'


class Groundwatersampledetails(models.Model):
    idgroundwatersampledetails = models.IntegerField(db_column='idGroundwaterSampleDetails', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName')  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    idfieldtrip = models.IntegerField(db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroundwaterSampleDetails'


class Incaveraingauge(models.Model):
    idincaveraingauge = models.IntegerField(db_column='idInCaveRainGauge', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    dripinterval = models.TextField(db_column='DripInterval', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InCaveRainGauge'


class Lsicarbonateresults(models.Model):
    idlsicarbonateresults = models.IntegerField(db_column='idLSICarbonateResults', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.TextField(db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.TextField(db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    d18o = models.TextField(db_column='d18O', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d18oerror = models.TextField(db_column='d18OError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d13c = models.TextField(db_column='d13C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d13cerror = models.TextField(db_column='d13CError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.TextField(db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LSICarbonateResults'


class Lab(models.Model):
    idlab = models.IntegerField(db_column='idLab', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    labname = models.TextField(db_column='LabName', unique=True)  # Field name made lowercase.
    institution = models.TextField(db_column='Institution', blank=True, null=True)  # Field name made lowercase.
    pi = models.TextField(db_column='PI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lab'


class Labinstrument(models.Model):
    idlabinstrument = models.IntegerField(db_column='idLabInstrument', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    labinstrument = models.TextField(db_column='LabInstrument', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrument'


class Labinstrumentinterface(models.Model):
    idlabinstrumentinterface = models.IntegerField(db_column='idLabInstrumentInterface', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    labinstrumentinterface = models.TextField(db_column='LabInstrumentInterface', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentInterface'


class Labinstrumentrun(models.Model):
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    lab = models.TextField(db_column='Lab', blank=True, null=True)  # Field name made lowercase.
    labinstrument = models.TextField(db_column='LabInstrument', blank=True, null=True)  # Field name made lowercase.
    labinstrumentinterface = models.TextField(db_column='LabInstrumentInterface', blank=True, null=True)  # Field name made lowercase.
    analysis = models.TextField(db_column='Analysis', blank=True, null=True)  # Field name made lowercase.
    dateanalyzed = models.DateTimeField(db_column='DateAnalyzed', blank=True, null=True)  # Field name made lowercase.
    runby = models.TextField(db_column='RunBy', blank=True, null=True)  # Field name made lowercase.
    submittedby = models.TextField(db_column='SubmittedBy', blank=True, null=True)  # Field name made lowercase.
    labreport = models.TextField(db_column='LabReport', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentRun'


class Labinstrumentrunstandard(models.Model):
    idlabinstrumentrunstandard = models.IntegerField(db_column='idLabInstrumentRunStandard', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    labinstrumentstandard = models.TextField(db_column='LabInstrumentStandard', blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    error = models.TextField(db_column='Error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    units = models.TextField(db_column='Units', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentRunStandard'


class Labinstrumentstandard(models.Model):
    idlabinstrumentstandard = models.IntegerField(db_column='idLabInstrumentStandard', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    labinstrumentstandard = models.TextField(db_column='LabInstrumentStandard', unique=True, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentStandard'


class Location(models.Model):
    idlocation = models.IntegerField(db_column='idLocation', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Platefielddata(models.Model):
    idplatefielddata = models.IntegerField(db_column='idPlateFieldData', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    deployfieldtrip = models.IntegerField(db_column='DeployFieldTrip', blank=True, null=True)  # Field name made lowercase.
    datedeploy = models.DateTimeField(db_column='DateDeploy', blank=True, null=True)  # Field name made lowercase.
    dateremove = models.DateTimeField(db_column='DateRemove', blank=True, null=True)  # Field name made lowercase.
    datereplace = models.DateTimeField(db_column='DateReplace', blank=True, null=True)  # Field name made lowercase.
    datecollect = models.DateTimeField(db_column='DateCollect', blank=True, null=True)  # Field name made lowercase.
    collectfieldtrip = models.IntegerField(db_column='CollectFieldTrip', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlateFieldData'


class Platefinalweight(models.Model):
    idplatefinalweight = models.IntegerField(db_column='idPlateFinalWeight', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    idplatestandardweight = models.IntegerField(db_column='idPlateStandardWeight', blank=True, null=True)  # Field name made lowercase.
    worker = models.TextField(db_column='Worker', blank=True, null=True)  # Field name made lowercase.
    finalweight = models.TextField(db_column='FinalWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateFinalWeight'


class Plateinitialweight(models.Model):
    idplateinitialweight = models.IntegerField(db_column='idPlateInitialWeight', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    idplatestandardweight = models.IntegerField(db_column='idPlateStandardWeight', blank=True, null=True)  # Field name made lowercase.
    worker = models.TextField(db_column='Worker', blank=True, null=True)  # Field name made lowercase.
    initialweight = models.TextField(db_column='InitialWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateInitialWeight'


class Platestandardweight(models.Model):
    idplatestandardweight = models.IntegerField(db_column='idPlateStandardWeight', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(db_column='Batch', blank=True, null=True)  # Field name made lowercase.
    standardweight = models.TextField(db_column='StandardWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateStandardWeight'


class Plateweightstandard(models.Model):
    idplateweightstandard = models.IntegerField(db_column='idPlateWeightStandard', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(db_column='Batch', blank=True, null=True)  # Field name made lowercase.
    weight1 = models.TextField(db_column='Weight1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight2 = models.TextField(db_column='Weight2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight3 = models.TextField(db_column='Weight3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight4 = models.TextField(db_column='Weight4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight5 = models.TextField(db_column='Weight5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateWeightStandard'


class Preservative(models.Model):
    idpreservative = models.IntegerField(db_column='idPreservative', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    preservative = models.TextField(db_column='Preservative', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preservative'


class Raincollection(models.Model):
    idraincollection = models.IntegerField(db_column='idRainCollection', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    datedeploy = models.DateTimeField(db_column='DateDeploy', blank=True, null=True)  # Field name made lowercase.
    datecollect = models.DateTimeField(db_column='DateCollect', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RainCollection'


class Rainsampledetails(models.Model):
    idrainsampledetails = models.IntegerField(db_column='idRainSampleDetails', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    idraincollection = models.IntegerField(db_column='idRainCollection', blank=True, null=True)  # Field name made lowercase.
    bottlename = models.TextField(db_column='BottleName', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RainSampleDetails'


class Samplenamemasterlist(models.Model):
    idsamplenamemasterlist = models.IntegerField(db_column='idSampleNameMasterList', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', unique=True)  # Field name made lowercase.
    sampletype = models.TextField(db_column='SampleType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleNameMasterList'


class Sampletype(models.Model):
    idsampletype = models.IntegerField(db_column='idSampleType', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    sampletype = models.TextField(db_column='SampleType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleType'


class Site(models.Model):
    idsite = models.IntegerField(db_column='idSite', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    site = models.TextField(db_column='Site', unique=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    sitetype = models.TextField(db_column='SiteType', blank=True, null=True)  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sitecode = models.TextField(db_column='SiteCode', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Site'


class Sitetype(models.Model):
    idsitetype = models.IntegerField(db_column='idSiteType', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    sitetype = models.TextField(db_column='SiteType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SiteType'


class Units(models.Model):
    idunits = models.IntegerField(db_column='idUnits', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    units = models.TextField(db_column='Units', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Units'


class Watersampleinventory(models.Model):
    idwatersampleinventory = models.IntegerField(db_column='idWaterSampleInventory', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    labelname = models.TextField(db_column='LabelName', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    bottlesize = models.TextField(db_column='BottleSize', blank=True, null=True)  # Field name made lowercase.
    bottletype = models.TextField(db_column='BottleType', blank=True, null=True)  # Field name made lowercase.
    preservative = models.TextField(db_column='Preservative', blank=True, null=True)  # Field name made lowercase.
    intendedanalysis = models.CharField(db_column='IntendedAnalysis', max_length=45, blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WaterSampleInventory'


class Worker(models.Model):
    idworker = models.IntegerField(db_column='idWorker', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    worker = models.TextField(db_column='Worker', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Worker'


class D18Owaterresults(models.Model):
    idd18owaterresults = models.IntegerField(db_column='idd18OWaterResults', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.TextField(db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.TextField(db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    d18o = models.TextField(db_column='d18O', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d18oerror = models.TextField(db_column='d18OError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.TextField(db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd18OWaterResults'


class D2Hwaterresults(models.Model):
    idd2hwaterresults = models.IntegerField(db_column='idd2HWaterResults', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    idlabinstrumentrun = models.IntegerField(db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.TextField(db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.TextField(db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.TextField(db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    d2h = models.TextField(db_column='d2H', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d2herror = models.TextField(db_column='d2HError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.TextField(db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd2HWaterResults'