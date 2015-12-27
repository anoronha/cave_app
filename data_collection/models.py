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
    idalkalinity = models.AutoField(db_column='idAlkalinity', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_Alkalinity_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    dateanalyzed = models.DateTimeField(db_column='DateAnalyzed', blank=True, null=True)  # Field name made lowercase.
    cartrige = models.IntegerField(db_column='Cartrige', blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(max_digits=10, decimal_places=5, db_column='Volume', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    starttemp = models.DecimalField(max_digits=10, decimal_places=5, db_column='StartTemp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startph = models.DecimalField(max_digits=10, decimal_places=5, db_column='StartpH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endtemp = models.DecimalField(max_digits=10, decimal_places=5, db_column='EndTemp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endph = models.DecimalField(max_digits=10, decimal_places=5, db_column='EndpH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    alkdigit = models.DecimalField(max_digits=10, decimal_places=5, db_column='AlkDigit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    alkalinity = models.DecimalField(max_digits=10, decimal_places=5, db_column='Alkalinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    workername = models.ForeignKey('Worker', to_field="workername", related_name="fk_Alkalinity_WorkerName", db_column='WorkerName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alkalinity'

    def __str__(self):
        return self.alkalinity


class Analysis(models.Model):
    idanalysis = models.AutoField(db_column='idAnalysis', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    analysis = models.CharField(max_length=50, db_column='Analysis', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Analysis'


class Analyte(models.Model):
    idanalyte = models.AutoField(db_column='idAnalyte', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    analyte = models.CharField(max_length=50, db_column='Analyte', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Analyte'


class Anionresults(models.Model):
    idanionresults = models.AutoField(db_column='idAnionResults', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idlabinstrumentrun = models.ForeignKey('Labinstrumentrun', to_field="idlabinstrumentrun", related_name="fk_AnionResults_LabInstrumentRun", db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_AnionResults_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.CharField(max_length=50, db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.ForeignKey('Units', to_field="units", related_name="fk_AnionResults_UnitsSample", db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    f = models.DecimalField(max_digits=10, decimal_places=5, db_column='F', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cl = models.DecimalField(max_digits=10, decimal_places=5, db_column='Cl', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    no2 = models.DecimalField(max_digits=10, decimal_places=5, db_column='NO2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    so4 = models.DecimalField(max_digits=10, decimal_places=5, db_column='SO4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    br = models.DecimalField(max_digits=10, decimal_places=5, db_column='Br', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    no3 = models.DecimalField(max_digits=10, decimal_places=5, db_column='NO3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    po4 = models.DecimalField(max_digits=10, decimal_places=5, db_column='PO4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.ForeignKey('Units', to_field="units", related_name="fk_AnionResults_UnitsResult", db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnionResults'


class Bottlesize(models.Model):
    idbottlesize = models.AutoField(db_column='idBottleSize', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    bottlesize = models.CharField(max_length=50, db_column='BottleSize', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BottleSize'

    def __str__(self):
        return self.bottlesize


class Bottletype(models.Model):
    idbottletype = models.AutoField(db_column='idBottleType', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    bottletype = models.CharField(max_length=50, db_column='BottleType', unique=True, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BottleType'

    def __str__(self):
        return self.bottletype


class Cationresults(models.Model):
    idcationresults = models.AutoField(db_column='idCationResults', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idlabinstrumentrun = models.ForeignKey('Labinstrumentrun', to_field="idlabinstrumentrun", related_name="fk_CationResults_LabInstrumentRun", db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_CationResults_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.DecimalField(max_digits=10, decimal_places=5, db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.ForeignKey('Units', to_field="units", related_name="fk_CationResults_UnitsSample", db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    li = models.DecimalField(max_digits=10, decimal_places=5, db_column='Li', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ag = models.DecimalField(max_digits=10, decimal_places=5, db_column='Ag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    al = models.DecimalField(max_digits=10, decimal_places=5, db_column='Al', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    as_field = models.DecimalField(max_digits=10, decimal_places=5, db_column='As', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word. This field type is a guess.
    b = models.DecimalField(max_digits=10, decimal_places=5, db_column='B', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ba = models.DecimalField(max_digits=10, decimal_places=5, db_column='Ba', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    be = models.DecimalField(max_digits=10, decimal_places=5, db_column='Be', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bi = models.DecimalField(max_digits=10, decimal_places=5, db_column='Bi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ca = models.DecimalField(max_digits=10, decimal_places=5, db_column='Ca', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cd = models.DecimalField(max_digits=10, decimal_places=5, db_column='Cd', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    co = models.DecimalField(max_digits=10, decimal_places=5, db_column='Co', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cr = models.DecimalField(max_digits=10, decimal_places=5, db_column='Cr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cs = models.DecimalField(max_digits=10, decimal_places=5, db_column='Cs', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cu = models.DecimalField(max_digits=10, decimal_places=5, db_column='Cu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fe = models.DecimalField(max_digits=10, decimal_places=5, db_column='Fe', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ge = models.DecimalField(max_digits=10, decimal_places=5, db_column='Ge', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    k = models.DecimalField(max_digits=10, decimal_places=5, db_column='K', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lu = models.DecimalField(max_digits=10, decimal_places=5, db_column='Lu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mg = models.DecimalField(max_digits=10, decimal_places=5, db_column='Mg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mn = models.DecimalField(max_digits=10, decimal_places=5, db_column='Mn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mo = models.DecimalField(max_digits=10, decimal_places=5, db_column='Mo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    na = models.DecimalField(max_digits=10, decimal_places=5, db_column='Na', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ni = models.DecimalField(max_digits=10, decimal_places=5, db_column='Ni', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    p = models.DecimalField(max_digits=10, decimal_places=5, db_column='P', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pb = models.DecimalField(max_digits=10, decimal_places=5, db_column='Pb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rb = models.DecimalField(max_digits=10, decimal_places=5, db_column='Rb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    s = models.DecimalField(max_digits=10, decimal_places=5, db_column='S', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sb = models.DecimalField(max_digits=10, decimal_places=5, db_column='Sb', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sc = models.DecimalField(max_digits=10, decimal_places=5, db_column='Sc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    se = models.DecimalField(max_digits=10, decimal_places=5, db_column='Se', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    si = models.DecimalField(max_digits=10, decimal_places=5, db_column='Si', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sn = models.DecimalField(max_digits=10, decimal_places=5, db_column='Sn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sr = models.DecimalField(max_digits=10, decimal_places=5, db_column='Sr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    te = models.DecimalField(max_digits=10, decimal_places=5, db_column='Te', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    th = models.DecimalField(max_digits=10, decimal_places=5, db_column='Th', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ti = models.DecimalField(max_digits=10, decimal_places=5, db_column='Ti', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tl = models.DecimalField(max_digits=10, decimal_places=5, db_column='Tl', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    u = models.DecimalField(max_digits=10, decimal_places=5, db_column='U', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    v = models.DecimalField(max_digits=10, decimal_places=5, db_column='V', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zn = models.DecimalField(max_digits=10, decimal_places=5, db_column='Zn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zr = models.DecimalField(max_digits=10, decimal_places=5, db_column='Zr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.ForeignKey('Units', to_field="units", related_name="fk_CationResults_UnitsResult", db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CationResults'


class Dripcollectionbottle(models.Model):
    iddripcollectionbottle = models.AutoField(db_column='idDripCollectionBottle', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_DripCollectionBottle_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    initialmass = models.DecimalField(max_digits=10, decimal_places=5, db_column='InitialMass', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    finalmass = models.DecimalField(max_digits=10, decimal_places=5, db_column='FinalMass', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deploytime = models.DateTimeField(db_column='DeployTime', blank=True, null=True)  # Field name made lowercase.
    collecttime = models.DateTimeField(db_column='CollectTime', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DripCollectionBottle'


class Dripinterval(models.Model):
    iddripinterval = models.AutoField(db_column='idDripInterval', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idfieldtrip = models.ForeignKey('Fieldtrip', to_field="idfieldtrip", related_name="fk_DripInterval_FieldTrip", db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_DripInterval_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    timecollected = models.DateTimeField(db_column='TimeCollected', blank=True, null=True)  # Field name made lowercase.
    count1 = models.IntegerField(db_column='Count1', blank=True, null=True)  # Field name made lowercase.
    count2 = models.IntegerField(db_column='Count2', blank=True, null=True)  # Field name made lowercase.
    count3 = models.IntegerField(db_column='Count3', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DripInterval'


class Dripperminute(models.Model):
    iddripperminute = models.AutoField(db_column='idDripPerMinute', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idfieldtrip = models.ForeignKey('Fieldtrip', to_field="idfieldtrip", related_name="fk_DripPerMin_FieldTrip", db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_DripPerMin_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    timecollected = models.DateTimeField(db_column='TimeCollected', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    minutes = models.IntegerField(db_column='Minutes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DripPerMinute'


class Fieldco2(models.Model):
    idfieldco2 = models.AutoField(db_column='idFieldCO2', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_FieldCO2_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.ForeignKey('Fieldinstrumentname', to_field="fieldinstrumentname", related_name="fk_FieldCO2_FieldInstrumentName", db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    lognumber = models.IntegerField(db_column='LogNumber', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    co2 = models.IntegerField(db_column='CO2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldCO2'


class Fieldco2Continous(models.Model):
    idfieldco2continous = models.AutoField(db_column='idFieldCO2Continous', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idfieldinstrumentdeployment = models.ForeignKey('Fieldinstrumentdeployment', to_field="idfieldinstrumentdeployment", related_name="fk_FieldCO2Continous_FieldInstrumentDeployment", db_column='idFieldInstrumentDeployment', blank=True, null=True)  # Field name made lowercase.
    lognumber = models.IntegerField(db_column='LogNumber', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    co2 = models.IntegerField(db_column='CO2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldCO2Continous'


class Fieldco2Spot(models.Model):
    idfieldco2spot = models.AutoField(db_column='idFieldCO2Spot', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idfieldtrip = models.ForeignKey('Fieldtrip', to_field="idfieldtrip", related_name="fk_FieldCO2Spot_FieldTrip", db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_FieldCO2Spot_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    fieldinstrumentname = models.ForeignKey('Fieldinstrumentname', to_field="fieldinstrumentname", related_name="fk_FieldCO2Spot_FieldInstrumentName", db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    co2 = models.IntegerField(db_column='CO2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldCO2Spot'


class Fieldinstruementservicerecord(models.Model):
    idfieldinstruementservicerecord = models.AutoField(db_column='idFieldInstruementServiceRecord', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumentname = models.ForeignKey('Fieldinstrumentname', to_field="fieldinstrumentname", related_name="fk_FieldInstruementServiceRecord_LoggerName", db_column='FieldInstrumentName')  # Field name made lowercase.
    dateshippedout = models.CharField(max_length=50, db_column='DateShippedOut')  # Field name made lowercase.
    datereturned = models.CharField(max_length=50, db_column='DateReturned', blank=True, null=True)  # Field name made lowercase.
    servicerecord = models.CharField(max_length=50, db_column='ServiceRecord', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstruementServiceRecord'


class Fieldinstrumentcomponent(models.Model):
    idfieldinstrumentcomponent = models.AutoField(db_column='idFieldInstrumentComponent', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=45, blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(max_length=50, db_column='PartNumber', blank=True, null=True)  # Field name made lowercase.
    partname = models.CharField(max_length=50, db_column='PartName', blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.
    datepurchased = models.DateTimeField(db_column='DatePurchased', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentComponent'


class Fieldinstrumentdeployment(models.Model):
    idfieldinstrumentdeployment = models.AutoField(db_column='idFieldInstrumentDeployment', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumentname = models.ForeignKey('Fieldinstrumentname', to_field="fieldinstrumentname", related_name="fk_FieldInstrumentDeployment_FieldInstrumentName", db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_FieldInstrumentDeployment_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    deployfieldtrip = models.ForeignKey('Fieldtrip', to_field="idfieldtrip", related_name="fk_FieldInstrumentDeployment_DeployFieldTrip", db_column='DeployFieldTrip', blank=True, null=True)  # Field name made lowercase.
    datedeploy = models.DateTimeField(db_column='DateDeploy', blank=True, null=True)  # Field name made lowercase.
    collectfieldtrip = models.ForeignKey('Fieldtrip', to_field="idfieldtrip", related_name="fk_FieldInstrumentDeployment_CollectFieldTrip", db_column='CollectFieldTrip', blank=True, null=True)  # Field name made lowercase.
    datecollect = models.DateTimeField(db_column='DateCollect', blank=True, null=True)  # Field name made lowercase.
    workerdeploy = models.CharField(max_length=50, db_column='WorkerDeploy', blank=True, null=True)  # Field name made lowercase.
    workercollect = models.CharField(max_length=50, db_column='WorkerCollect', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentDeployment'


class Fieldinstrumentdetails(models.Model):
    idfieldinstrumentdetails = models.AutoField(db_column='idFieldInstrumentDetails', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumentname = models.ForeignKey('Fieldinstrumentname', to_field="fieldinstrumentname", related_name="fk_FieldInstrumentDetails_FieldInstrumentName", db_column='FieldInstrumentName')  # Field name made lowercase.
    fieldinstrumentcomponent = models.ForeignKey(Fieldinstrumentcomponent, to_field="serialnumber", related_name="fk_FieldInstrumentDetails_FieldInstrumentComponent", db_column='FieldInstrumentComponent', blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.DateTimeField(db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentDetails'


class Fieldinstrumentname(models.Model):
    idfieldinstrumentname = models.AutoField(db_column='idFieldInstrumentName', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumentname = models.CharField(max_length=50, db_column='FieldInstrumentName', unique=True)  # Field name made lowercase.
    fieldinstrumenttype = models.ForeignKey('Fieldinstrumenttype', to_field="fieldinstrumenttype", related_name="fk_FieldInstrumentName_FieldInstrumentType", db_column='FieldInstrumentType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentName'

    def __str__(self):
        return self.fieldinstrumentname


class Fieldinstrumentservicerecord(models.Model):
    idfieldinstrumentservicerecord = models.AutoField(db_column='idFieldInstrumentServiceRecord', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumentname = models.ForeignKey(Fieldinstrumentname, to_field="fieldinstrumentname", related_name="fk_FieldInstrumentServiceRecord_LoggerName", db_column='FieldInstrumentName')  # Field name made lowercase.
    dateshippedout = models.CharField(max_length=50, db_column='DateShippedOut')  # Field name made lowercase.
    datereturned = models.CharField(max_length=50, db_column='DateReturned', blank=True, null=True)  # Field name made lowercase.
    servicerecord = models.CharField(max_length=50, db_column='ServiceRecord', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentServiceRecord'


class Fieldinstrumenttype(models.Model):
    idfieldinstrumenttype = models.AutoField(db_column='idFieldInstrumentType', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumenttype = models.CharField(max_length=50, db_column='FieldInstrumentType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldInstrumentType'


class Fieldteam(models.Model):
    idfieldteam = models.AutoField(db_column='idFieldTeam', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    workername = models.ForeignKey('Worker', to_field="workername", related_name="fk_FieldTeam_WorkerName", db_column='WorkerName')  # Field name made lowercase.
    idfieldtrip = models.ForeignKey('Fieldtrip', to_field="idfieldtrip", related_name="fk_FieldTeam_idFieldTrip", db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldTeam'


class Fieldtrip(models.Model):
    idfieldtrip = models.AutoField(db_column='idFieldTrip', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    location = models.ForeignKey('Location', to_field="location", related_name="fk_FieldTrip_Location", db_column='Location', blank=True, null=True)  # Field name made lowercase.
    beginfieldtrip = models.DateTimeField(db_column='BeginFieldTrip', blank=True, null=True)  # Field name made lowercase.
    endfieldtrip = models.DateTimeField(db_column='EndFieldTrip', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldTrip'


    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))

        return ', '.join(sb)



class Fieldwaterchemistry(models.Model):
    idfieldwaterchemistry = models.AutoField(db_column='idFieldWaterChemistry', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    fieldinstrumentname = models.CharField(max_length=50, db_column='FieldInstrumentName', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_FieldWaterChemistry_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    orp = models.DecimalField(max_digits=10, decimal_places=5, db_column='ORP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tds = models.DecimalField(max_digits=10, decimal_places=5, db_column='TDS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conductivity = models.DecimalField(max_digits=10, decimal_places=5, db_column='Conductivity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ph = models.DecimalField(max_digits=10, decimal_places=5, db_column='pH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp = models.DecimalField(max_digits=10, decimal_places=5, db_column='Temp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    salinity = models.DecimalField(max_digits=10, decimal_places=5, db_column='Salinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldWaterChemistry'


class Fieldweatherstationdata(models.Model):
    idfieldweatherstationdata = models.AutoField(db_column='idFieldWeatherStationData', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idfieldinstrumentdeployment = models.ForeignKey(Fieldinstrumentdeployment, to_field="idfieldinstrumentdeployment", related_name="fk_FieldWeatherStationData_FieldInstrumentDeployment", db_column='idFieldInstrumentDeployment', blank=True, null=True)  # Field name made lowercase.
    lognumber = models.IntegerField(db_column='LogNumber', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    temp = models.DecimalField(max_digits=10, decimal_places=5, db_column='Temp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rh = models.DecimalField(max_digits=10, decimal_places=5, db_column='RH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pressure = models.DecimalField(max_digits=10, decimal_places=5, db_column='Pressure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldWeatherStationData'


class Groundwatersampledetails(models.Model):
    idgroundwatersampledetails = models.AutoField(db_column='idGroundwaterSampleDetails', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_GroundwaterSampleDetails_SampleName", db_column='SampleName')  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_GroundwaterSampleDetails_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    idfieldtrip = models.ForeignKey(Fieldtrip, to_field="idfieldtrip", related_name="fk_GroundwaterSampleDetails_FieldTrip", db_column='idFieldTrip', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GroundwaterSampleDetails'


class Incaveraingauge(models.Model):
    idincaveraingauge = models.AutoField(db_column='idInCaveRainGauge', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_InCaveRainGauge_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    dripinterval = models.CharField(max_length=500, db_column='DripInterval', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InCaveRainGauge'

class Institution(models.Model):
    idinstitution = models.AutoField(db_column='idInstitution', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    institution = models.CharField(max_length=50, db_column='Institution', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Institution'

    def __str__(self):
        return self.institution


class Jobtitle(models.Model):
    idjobtitle = models.AutoField(db_column='idJobTitle', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    jobtitle = models.CharField(max_length=50, db_column='JobTitle', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JobTitle'

    def __str__(self):
        return self.jobtitle

class Lsicarbonateresults(models.Model):
    idlsicarbonateresults = models.AutoField(db_column='idLSICarbonateResults', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idlabinstrumentrun = models.ForeignKey('Labinstrumentrun', to_field="idlabinstrumentrun", related_name="fk_LSICarbonateResults_LabInstrumentRun", db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_LSICarbonateResults_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.CharField(max_length=50, db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.ForeignKey('Units', to_field="units", related_name="fk_LSICarbonateResults_UnitsSample", db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    d18o = models.DecimalField(max_digits=10, decimal_places=5, db_column='d18O', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d18oerror = models.DecimalField(max_digits=10, decimal_places=5, db_column='d18OError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d13c = models.DecimalField(max_digits=10, decimal_places=5, db_column='d13C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d13cerror = models.DecimalField(max_digits=10, decimal_places=5, db_column='d13CError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.ForeignKey('Units', to_field="units", related_name="fk_LSICarbonateResults_UnitsResult", db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LSICarbonateResults'


class Lab(models.Model):
    idlab = models.AutoField(db_column='idLab', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    labname = models.CharField(max_length=50, db_column='LabName', unique=True)  # Field name made lowercase.
    institution = models.ForeignKey(Institution, to_field="institution", related_name="fk_Lab_Institution", db_column='Institution', blank=True, null=True)  # Field name made lowercase.
    pi = models.ForeignKey('Worker', to_field="workername", related_name="fk_Lab_PI", db_column='PI', blank=True, null=True)  # Field name made lowercase.
    active = models.NullBooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lab'

    def __str__(self):
        return self.labname


class Labinstrument(models.Model):
    idlabinstrument = models.AutoField(db_column='idLabInstrument', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    labinstrument = models.CharField(max_length=50, db_column='LabInstrument', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrument'


class Labinstrumentinterface(models.Model):
    idlabinstrumentinterface = models.AutoField(db_column='idLabInstrumentInterface', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    labinstrumentinterface = models.CharField(max_length=50, db_column='LabInstrumentInterface', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentInterface'


class Labinstrumentrun(models.Model):
    idlabinstrumentrun = models.AutoField(db_column='idLabInstrumentRun', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    lab = models.ForeignKey(Lab, to_field="labname", related_name="fk_LabInstrumentRun_Lab", db_column='Lab', blank=True, null=True)  # Field name made lowercase.
    labinstrument = models.ForeignKey(Labinstrument, to_field="labinstrument", related_name="fk_LabInstrumentRun_LabInstrument", db_column='LabInstrument', blank=True, null=True)  # Field name made lowercase.
    labinstrumentinterface = models.ForeignKey(Labinstrumentinterface, to_field="labinstrumentinterface", related_name="fk_LabInstrumentRun_InstrumentInterface", db_column='LabInstrumentInterface', blank=True, null=True)  # Field name made lowercase.
    analysis = models.ForeignKey(Analysis, to_field="analysis", related_name="fk_LabInstrumentRun_Analysis", db_column='Analysis', blank=True, null=True)  # Field name made lowercase.
    dateanalyzed = models.DateTimeField(db_column='DateAnalyzed', blank=True, null=True)  # Field name made lowercase.
    runby = models.CharField(max_length=50, db_column='RunBy', blank=True, null=True)  # Field name made lowercase.
    submittedby = models.ForeignKey('Worker', to_field="workername", related_name="fk_LabInstrumentRun_SubmittedBy", db_column='SubmittedBy', blank=True, null=True)  # Field name made lowercase.
    labreport = models.CharField(max_length=50, db_column='LabReport', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=50, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentRun'


class Labinstrumentrunstandard(models.Model):
    idlabinstrumentrunstandard = models.AutoField(db_column='idLabInstrumentRunStandard', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idlabinstrumentrun = models.ForeignKey(Labinstrumentrun, to_field="idlabinstrumentrun", related_name="fk_LabInstrumentRunStandard_LabInstrumentRun", db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    labinstrumentstandard = models.ForeignKey('Labinstrumentstandard', to_field="labinstrumentstandard", related_name="fk_LabInstrumentRunStandard_LabInstrumentStandard", db_column='LabInstrumentStandard', blank=True, null=True)  # Field name made lowercase.
    value = models.DecimalField(max_digits=10, decimal_places=5, db_column='Value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    error = models.DecimalField(max_digits=10, decimal_places=5, db_column='Error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    units = models.CharField(max_length=50, db_column='Units', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentRunStandard'


class Labinstrumentstandard(models.Model):
    idlabinstrumentstandard = models.AutoField(db_column='idLabInstrumentStandard', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    labinstrumentstandard = models.CharField(max_length=50, db_column='LabInstrumentStandard', unique=True, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=50, db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LabInstrumentStandard'


class Location(models.Model):
    idlocation = models.AutoField(db_column='idLocation', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    location = models.CharField(max_length=50, db_column='Location', unique=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    locationtype = models.ForeignKey('Locationtype', to_field="locationtype", related_name="fk_Location_LocationType", db_column='LocationType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'

    def __str__(self):
        return self.location


class Locationtype(models.Model):
    idlocationtype = models.AutoField(db_column='idLocationType', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    locationtype = models.CharField(max_length=50, db_column='LocationType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LocationType'

    def __str__(self):
        return self.locationtype


class Platefielddata(models.Model):
    idplatefielddata = models.AutoField(db_column='idPlateFieldData', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_PlateFieldData_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_PlateFieldData_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    deployfieldtrip = models.ForeignKey(Fieldtrip, to_field="idfieldtrip", related_name="fk_PlateFieldData_DeployFieldTrip", db_column='DeployFieldTrip', blank=True, null=True)  # Field name made lowercase.
    datedeploy = models.DateTimeField(db_column='DateDeploy', blank=True, null=True)  # Field name made lowercase.
    dateremove = models.DateTimeField(db_column='DateRemove', blank=True, null=True)  # Field name made lowercase.
    datereplace = models.DateTimeField(db_column='DateReplace', blank=True, null=True)  # Field name made lowercase.
    datecollect = models.DateTimeField(db_column='DateCollect', blank=True, null=True)  # Field name made lowercase.
    collectfieldtrip = models.ForeignKey(Fieldtrip, to_field="idfieldtrip", related_name="fk_PlateFieldData_CollectFieldTrip", db_column='CollectFieldTrip', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlateFieldData'


class Platefinalweight(models.Model):
    idplatefinalweight = models.AutoField(db_column='idPlateFinalWeight', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_PlateFinalWeight_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    idplatestandardweight = models.ForeignKey('Platestandardweight', to_field="idplatestandardweight", related_name="fk_idPlateFinalWeight_PlateStandardWeight", db_column='idPlateStandardWeight', blank=True, null=True)  # Field name made lowercase.
    workername = models.ForeignKey('Worker', to_field="workername", related_name="fk_PlateFinalWeight_WorkerName", db_column='WorkerName', blank=True, null=True)  # Field name made lowercase.
    finalweight = models.DecimalField(max_digits=10, decimal_places=5, db_column='FinalWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlateFinalWeight'


class Plateinitialweight(models.Model):
    idplateinitialweight = models.AutoField(db_column='idPlateInitialWeight', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_PlateInitialWeight_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    idplatestandardweight = models.ForeignKey('Platestandardweight', to_field="idplatestandardweight", related_name="fk_idPlateInitialWeight_PlateStandardWeight", db_column='idPlateStandardWeight', blank=True, null=True)  # Field name made lowercase.
    workername = models.ForeignKey('Worker', to_field="workername", related_name="fk_PlateInitialWeight_WorkerName", db_column='WorkerName', blank=True, null=True)  # Field name made lowercase.
    initialweight = models.DecimalField(max_digits=10, decimal_places=5, db_column='InitialWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateInitialWeight'


class Platestandardweight(models.Model):
    idplatestandardweight = models.AutoField(db_column='idPlateStandardWeight', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(db_column='Batch', blank=True, null=True)  # Field name made lowercase.
    standardweight = models.DecimalField(max_digits=10, decimal_places=5, db_column='StandardWeight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateStandardWeight'


class Plateweightstandard(models.Model):
    idplateweightstandard = models.AutoField(db_column='idPlateWeightStandard', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    batch = models.IntegerField(db_column='Batch', blank=True, null=True)  # Field name made lowercase.
    weight1 = models.DecimalField(max_digits=10, decimal_places=5, db_column='Weight1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight2 = models.DecimalField(max_digits=10, decimal_places=5, db_column='Weight2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight3 = models.DecimalField(max_digits=10, decimal_places=5, db_column='Weight3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight4 = models.DecimalField(max_digits=10, decimal_places=5, db_column='Weight4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight5 = models.DecimalField(max_digits=10, decimal_places=5, db_column='Weight5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PlateWeightStandard'


class Preservative(models.Model):
    idpreservative = models.AutoField(db_column='idPreservative', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    preservative = models.CharField(max_length=50, db_column='Preservative', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Preservative'

    def __str__(self):
        return self.preservative


class Raincollection(models.Model):
    idraincollection = models.AutoField(db_column='idRainCollection', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    site = models.ForeignKey('Site', to_field="site", related_name="fk_RainCollection_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    datedeploy = models.DateTimeField(db_column='DateDeploy', blank=True, null=True)  # Field name made lowercase.
    datecollect = models.DateTimeField(db_column='DateCollect', blank=True, null=True)  # Field name made lowercase.
    workername = models.ForeignKey('Worker', to_field="workername", related_name="fk_RainCollection_WorkerName", db_column='WorkerName', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RainCollection'


class Rainsampledetails(models.Model):
    idrainsampledetails = models.AutoField(db_column='idRainSampleDetails', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.ForeignKey('Samplenamemasterlist', to_field="samplename", related_name="fk_RainSampleDetails_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    idraincollection = models.IntegerField(db_column='idRainCollection', blank=True, null=True)  # Field name made lowercase.
    bottlename = models.CharField(max_length=50, db_column='BottleName', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RainSampleDetails'


class Samplenamemasterlist(models.Model):
    idsamplenamemasterlist = models.AutoField(db_column='idSampleNameMasterList', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    samplename = models.CharField(max_length=50, db_column='SampleName', unique=True)  # Field name made lowercase.
    sampletype = models.ForeignKey('Sampletype', to_field="sampletype", related_name="fk_SampleNameMasterList_SampleType", db_column='SampleType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleNameMasterList'

    def __str__(self):
        return self.samplename


class Sampletype(models.Model):
    idsampletype = models.AutoField(db_column='idSampleType', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    sampletype = models.CharField(max_length=50, db_column='SampleType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SampleType'

    def __str__(self):
        return self.sampletype


class Site(models.Model):
    idsite = models.AutoField(db_column='idSite', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    site = models.CharField(max_length=50, db_column='Site', unique=True)  # Field name made lowercase.
    location = models.ForeignKey(Location, to_field="location", related_name="fk_Site_Location", db_column='Location', blank=True, null=True)  # Field name made lowercase.
    sitetype = models.ForeignKey('Sitetype', to_field="sitetype", related_name="fk_Site_SiteType", db_column='SiteType', blank=True, null=True)  # Field name made lowercase.
    xlocation = models.DecimalField(max_digits=20, decimal_places=10, db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocation = models.DecimalField(max_digits=20, decimal_places=10, db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sitecode = models.CharField(max_length=50, db_column='SiteCode', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Site'

    def __str__(self):
        return self.site


class Sitetype(models.Model):
    idsitetype = models.AutoField(db_column='idSiteType', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    sitetype = models.CharField(max_length=50, db_column='SiteType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SiteType'
        verbose_name = 'Site Type'
        verbose_name_plural = 'Site Types'

    def __str__(self):
        return self.sitetype

class Tippingbucketdata(models.Model):
    idtippingbucketdata = models.AutoField(db_column='idTippingBucketData', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    site = models.ForeignKey(Site, to_field="site", related_name="fk_TippingBucketData_Site", db_column='Site', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='Datetime', blank=True, null=True)  # Field name made lowercase.
    dripinterval = models.CharField(max_length=50, db_column='DripInterval', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TippingBucketData'


class Units(models.Model):
    idunits = models.AutoField(db_column='idUnits', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    units = models.CharField(max_length=50, db_column='Units', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Units'

    def __str__(self):
        return self.units

class Watersampleinventory(models.Model):
    idwatersampleinventory = models.AutoField(db_column='idWaterSampleInventory', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    labelname = models.CharField(max_length=50, db_column='LabelName', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey(Samplenamemasterlist, to_field="samplename", related_name="fk_WaterSampleInventory_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    bottlesize = models.ForeignKey(Bottlesize, to_field="bottlesize", related_name="fk_WaterSampleInventory_BottleSize", db_column='BottleSize', blank=True, null=True)  # Field name made lowercase.
    bottletype = models.ForeignKey(Bottletype, to_field="bottletype", related_name="fk_WaterSampleInventory_BottleType", db_column='BottleType', blank=True, null=True)  # Field name made lowercase.
    preservative = models.ForeignKey(Preservative, to_field="preservative", related_name="fk_WaterSampleInventory_Preservative", db_column='Preservative', blank=True, null=True)  # Field name made lowercase.
    intendedanalysis = models.ForeignKey(Analysis, to_field="analysis", related_name="fk_WaterSampleInventory_IntendedAnalysis", db_column='IntendedAnalysis', blank=True, null=True)  # Field name made lowercase.
    fillamount = models.DecimalField(max_digits=10, decimal_places=5, db_column='FillAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    note = models.CharField(max_length=500, db_column='Note', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WaterSampleInventory'


class Worker(models.Model):
    idworker = models.AutoField(db_column='idWorker', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    workername = models.CharField(max_length=50, db_column='WorkerName', unique=True)  # Field name made lowercase.
    workertype = models.ForeignKey('Workertype', to_field="workertype", related_name="fk_Worker_WorkerType", db_column='WorkerType', blank=True, null=True)  # Field name made lowercase.
    affiliation = models.ForeignKey('Institution', to_field="institution", related_name="fk_Worker_Affiliation", db_column='Affiliation', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.ForeignKey(Jobtitle, to_field="jobtitle", related_name="fk_Worker_JobTitle", db_column='JobTitle', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True)  # Field name made lowercase.
    email = models.CharField(max_length=50, db_column='Email', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(max_length=50, db_column='PhoneNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Worker'

    def __str__(self):
        return self.workername


class Workertype(models.Model):
    idworkertype = models.AutoField(db_column='idWorkerType', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    workertype = models.CharField(max_length=50, db_column='WorkerType', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WorkerType'

    def __str__(self):
        return self.workertype

class D18Owaterresults(models.Model):
    idd18owaterresults = models.AutoField(db_column='idd18OWaterResults', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idlabinstrumentrun = models.ForeignKey(Labinstrumentrun, to_field="idlabinstrumentrun", related_name="fk_d18OWaterResults_LabInstrumentRun", db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey(Samplenamemasterlist, to_field="samplename", related_name="fk_d18OWaterResults_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.CharField(max_length=50, db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.ForeignKey(Units, to_field="units", related_name="fk_d18OWaterResults_UnitsSample", db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    d18o = models.DecimalField(max_digits=10, decimal_places=5, db_column='d18O', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d18oerror = models.DecimalField(max_digits=10, decimal_places=5, db_column='d18OError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.ForeignKey(Units, to_field="units", related_name="fk_d18OWaterResults_UnitsResult", db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd18OWaterResults'


class D2Hwaterresults(models.Model):
    idd2hwaterresults = models.AutoField(db_column='idd2HWaterResults', primary_key=True, blank=False, null=False)  # Field name made lowercase.
    idlabinstrumentrun = models.ForeignKey(Labinstrumentrun, to_field="idlabinstrumentrun", related_name="fk_d2HWaterResults_LabInstrumentRun", db_column='idLabInstrumentRun', blank=True, null=True)  # Field name made lowercase.
    runposition = models.IntegerField(db_column='RunPosition', blank=True, null=True)  # Field name made lowercase.
    samplename = models.ForeignKey(Samplenamemasterlist, to_field="samplename", related_name="fk_d2HWaterResults_SampleName", db_column='SampleName', blank=True, null=True)  # Field name made lowercase.
    samplesize = models.DecimalField(max_digits=10, decimal_places=5, db_column='SampleSize', blank=True, null=True)  # Field name made lowercase.
    unitssample = models.ForeignKey(Units, to_field="units", related_name="fk_d2HWaterResults_UnitsSample", db_column='UnitsSample', blank=True, null=True)  # Field name made lowercase.
    d2h = models.DecimalField(max_digits=10, decimal_places=5, db_column='d2H', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    d2herror = models.DecimalField(max_digits=10, decimal_places=5, db_column='d2HError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unitsresult = models.ForeignKey(Units, to_field="units", related_name="fk_d2HWaterResults_UnitsResult", db_column='UnitsResult', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd2HWaterResults'
