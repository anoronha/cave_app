from django.shortcuts import render
from data_collection.models import *
from django.shortcuts import get_object_or_404
from data_collection.my_functions import *
from time import strftime
from django.http import HttpResponseRedirect
from data_collection.forms import *
from django.forms import formset_factory
import datetime

def index(request):
    return render(request, 'index.html')

def new_fieldtrip(request):
    if request.method == 'POST':
        form = NewFieldtripForm(request.POST)
        if form.is_valid():
            data = form.save()
            request.session["idfieldtrip_curr"] = data.pk
            return HttpResponseRedirect('/new-fieldtrip/select-sites/')
    else:
        form = NewFieldtripForm()
    return render(request, 'new_fieldtrip.html', {'form': form})

def new_fieldtrip_sites(request):
    if request.method == 'POST':
        sites_form = SelectWaterSampleSiteForm(request.POST)
        worker_form = SelectteamForm(request.POST)
        trip_date = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).endfieldtrip
        trip_date = trip_date.strftime('%Y%m%d')
        samplenames_curr = {}
        for key in request.POST.getlist('selected_sites'):
            sitecode = Site.objects.get(idsite=key).sitecode
            site = Site.objects.get(idsite=key).site
            samplename = '%s %s' %(trip_date, sitecode)
            masterlist_input = {'samplename': samplename, 'sampletype': 'groundwater'}
            sampledetail_input = {'samplename': samplename, 'site': site, 'idfieldtrip': request.session["idfieldtrip_curr"]}
            masterlist_form = SamplenamemasterlistForm(masterlist_input)
            sampledetail_form = GroundwatersampledetailsForm(sampledetail_input)
            samplenames_curr[site] = samplename
            if masterlist_form.is_valid():
                data = masterlist_form.save()
            if sampledetail_form.is_valid():
                data = sampledetail_form.save()
        for key in request.POST.getlist('workers'):
            workername = Worker.objects.get(idworker=key).workername
            worker_input = {'workername': workername, 'idfieldtrip': request.session["idfieldtrip_curr"]}
            print(worker_input)
            fieldteam_form = FieldteamForm(worker_input)
            if fieldteam_form.is_valid():
                data = fieldteam_form.save()

        request.session["samplenames_curr"] = samplenames_curr
        location = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).location
        return HttpResponseRedirect('/enter-site-data/')
    else:
        fieldtrip = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"])
        filtered_sites = Site.objects.exclude(active=0).exclude(sitetype='cave room').filter(location=fieldtrip.location)
        workers = Worker.objects.exclude(active=0).exclude(workertype='lab').exclude(workertype='supervisory')
        sites_form = SelectWaterSampleSiteForm(filtered_sites=filtered_sites)
        worker_form = SelectteamForm(workers=workers)
    return render(request, 'new_fieldtrip_sites.html', {'sites_form': sites_form,
                                                        'worker_form': worker_form,
                                                        })

def next_site_data(request):
    idfieldtrip_curr = request.session["idfieldtrip_curr"]
    start_trip = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).beginfieldtrip
    end_trip = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).endfieldtrip
    if (start_trip.day == end_trip.day) and (start_trip.month == end_trip.month):
        trip_days = ((datetime.datetime(start_trip.year, start_trip.month, start_trip.day), 'One Day Trip'))
    else:
        trip_days = ((datetime.datetime(start_trip.year, start_trip.month, start_trip.day), 'Day 1'),
                     (datetime.datetime(end_trip.year, end_trip.month, end_trip.day), 'Day 2'))

    initial_bottle_weights = {'Stumpy': '102.3',
                              'Stumpys Brother': '68.2',
                              'Station 1': '35.9',
                              'Station 2': '57.8',
                              'Flatman': '101.8',
                              'Trinity': '102.6',
                            }
    current_idx = request.session.get("current_sample_idx", 0)

    print(current_idx)
    if current_idx >= len(request.session["samplenames_curr"]):
        print("Deleting it!")
        del request.session["current_sample_idx"]
        return None

    key = sorted(request.session["samplenames_curr"])[current_idx]

    request.session["current_sample_idx"] = current_idx + 1

    samplename = request.session["samplenames_curr"][key]
    site = key


    srcat_initial = {'samplename': samplename,
                      'bottlesize': '30 mL',
                      'bottletype': 'HDPE vial',
                      'preservative': 'seastar nitric',
                      'intendedanalysis': 'cations'}
    anions_initial = {'samplename': samplename,
                      'bottlesize': '15 mL',
                      'bottletype': 'HDPE vial',
                      'preservative': 'refrigeration',
                      'intendedanalysis': 'anions'}
    d18O_initial = {'samplename': samplename,
                      'bottlesize': '4 mL',
                      'bottletype': 'glass vial',
                      'preservative': 'refrigeration',
                      'intendedanalysis': 'water d18O'}
    dD_initial = {'samplename': samplename,
                      'bottlesize': '4 mL',
                      'bottletype': 'glass vial',
                      'preservative': 'refrigeration',
                      'intendedanalysis': 'water d2H'}
    alk_initial = {'samplename': samplename,
                      'bottlesize': '30 mL',
                      'bottletype': 'crimp top bottle',
                      'preservative': 'none',
                      'intendedanalysis': 'alkalinity'}
    d13C_initial = {'samplename': samplename,
                      'bottlesize': '13 mL',
                      'bottletype': 'LabCo Exetainer',
                      'preservative': 'phosphoric acid',
                      'intendedanalysis': 'DIC d13C'}

    analysis_display = {
        "water d18O": u'&delta;<sup>18</sup>O',
        "water d2H": u'&delta;<sup>2</sup>H',
        "anions": u'Anions',
        "cations": u'Cations',
        "DIC d13C" : u'&delta;<sup>13</sup>C',
        "alkalinity" : u'Alkalinity',
    }
    fieldchem_form = FieldwaterchemistryForm(samplename=samplename)

    WatersampleinventoryFormset = formset_factory(WatersampleinventoryForm, extra=0)
    formset = WatersampleinventoryFormset(initial = [
        srcat_initial,
        anions_initial,
        d18O_initial,
        dD_initial,
        alk_initial,
        d13C_initial
    ])

    if key  == 'Pool':
        return render(request, 'enter_site_data.html', {'fieldchem_form': fieldchem_form,
                                                        'samplename': samplename,
                                                        'watersamples': formset,
                                                        })
    else:
        if key == 'Trinity':
            initialmass = initial_bottle_weights[key]
            bottle_initial = {'samplename': samplename,
                              'initialmass': initialmass,
                              'deploytime': end_trip,
                              'collecttime': end_trip,}
        else:
            initialmass = initial_bottle_weights[key]
            bottle_initial = {'samplename': samplename,
                              'initialmass': initialmass,
                              'deploytime': start_trip,
                              'collecttime': end_trip,}
        platedeploy_prev = Platefielddata.objects.filter(site=site).order_by('-idplatefielddata')[0]
        bottlecollection_form = DripcollectionbottleForm(initial=bottle_initial)
        bottle_down = DateTimeSplitForm(choices=trip_days)
        bottle_up = DateTimeSplitForm(choices=trip_days)
        dripinterval_form = DripintervalForm(site=site, idfieldtrip=idfieldtrip_curr, initial={'timecollected':start_trip})
        platecollect_form = PlatecollectForm(instance=platedeploy_prev)
        platedeploy_form = PlatedeplyForm(site=site, idfieldtrip=idfieldtrip_curr)
        fieldchem_form = FieldwaterchemistryForm(samplename=samplename)
        return render(request, 'enter_site_data.html', {'bottlecollection_form': bottlecollection_form,
                                                        'bottle_down':bottle_down,
                                                        'bottle_up':bottle_up,
                                                        'dripinterval_form': dripinterval_form,
                                                        'platecollect_form': platecollect_form,
                                                        'platedeploy_form': platedeploy_form,
                                                        'fieldchem_form': fieldchem_form,
                                                        'site': site,
                                                        'samplename': samplename,
                                                        'start_trip': start_trip,
                                                        'end_trip': end_trip,
                                                        'watersamples': formset,
                                                        'analysis_display': analysis_display,
                                                        # 'srcat_sample_form': srcat_sample_form,
                                                        # 'anions_sample_form': anions_sample_form,
                                                        # 'd18O_sample_form': d18O_sample_form,
                                                        # 'dD_sample_form': dD_sample_form,
                                                        # 'alk_sample_form': alk_sample_form,
                                                        # 'd13C_sample_form': d13C_sample_form,
                                                        })

def enter_site_data(request):
    if request.method == 'POST':
        bottlecollection_form = DripcollectionbottleForm(request.POST)
        dripinterval_form = DripintervalForm(request.POST)
        platecollect_form = PlatecollectForm(request.POST)
        platedeploy_form = PlatedeplyForm(request.POST)
        fieldchem_form = FieldwaterchemistryForm(request.POST)
        WatersampleinventoryFormset = formset_factory(WatersampleinventoryForm, extra=0)
        watersamples = WatersampleinventoryFormset(request.POST)
        if bottlecollection_form.is_valid():
            data = bottlecollection_form.save()
        if dripinterval_form.is_valid():
            data = dripinterval_form.save()
        if platecollect_form.is_valid():
            data = platecollect_form.save()
        if platedeploy_form.is_valid():
            data = platedeploy_form.save()
        if fieldchem_form.is_valid():
            data = fieldchem_form.save()
        if watersamples.is_valid():
            data = watersamples.save()
        next_site = next_site_data(request)
        if next_site:
            return next_site
        else:
            return HttpResponseRedirect('/samples-collected/')
    else:
        del request.session["current_sample_idx"]
        next_site = next_site_data(request)
        if next_site:
            return next_site
        else:
            return HttpResponseRedirect('/errar/')

def alk(request):
    form = AlkalinityForm()
    return render(request, 'alk.html', {'form': form})

def field_instruments(request):
    idfieldtrip_curr = request.session["idfieldtrip_curr"]
    NWR = {'idfieldtrip': idfieldtrip_curr, 'site': 'Spot Check Tree'}
    cave_entrance = {'idfieldtrip': idfieldtrip_curr, 'site': 'Cave Entrance'}
    ante_room = {'idfieldtrip': idfieldtrip_curr, 'site': 'Ante room'}
    mid_slide = {'idfieldtrip': idfieldtrip_curr, 'site': 'Mid Slide'}
    shakey_room = {'idfieldtrip': idfieldtrip_curr, 'site': 'Shakey Room'}
    big_room = {'idfieldtrip': idfieldtrip_curr, 'site': 'Big Room'}
    Fieldco2SpotFormset = formset_factory(Fieldco2SpotForm, extra=0, formset = BaseFieldco2SpotFormset)
    spotcheck_formset = Fieldco2SpotFormset(initial = [
                                                        NWR,
                                                        cave_entrance,
                                                        ante_room,
                                                        mid_slide,
                                                        shakey_room,
                                                        big_room,
                                                    ])

    upload_form = UploadFileForm()
    return render(request, 'field_instruments.html', {'upload_form': upload_form,'spotcheck_formset': spotcheck_formset})
