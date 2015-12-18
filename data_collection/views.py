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
        trip_input = {'location':Location.objects.get(pk=request.POST.get('location')),
                      'beginfieldtrip':request.POST.get('beginfieldtrip'),
                      'endfieldtrip':request.POST.get('endfieldtrip')}
        #right now I'm using a form to do this input because I can't figure out how to get the pk just by putting it straight into the model
        tmp = FieldtripForm(trip_input)
        if tmp.is_valid():
            data = tmp.save()
            request.session["idfieldtrip_curr"] = data.pk
        for key in request.POST.getlist('workers'):
            worker_input = Fieldteam(workername=Worker.objects.get(idworker=key),
                                     idfieldtrip=Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"])).save()
        return HttpResponseRedirect('/new-fieldtrip/select-sites/')
    else:
        workers = Worker.objects.exclude(active=0).exclude(workertype='lab').exclude(workertype='supervisory')
        trip_form = NewFieldtripForm(workers=workers)
    return render(request, 'new_fieldtrip.html', {'trip_form': trip_form,})

def new_fieldtrip_sites(request):
    #eventually want to change this to be dynamically generated on the previous page, so once you pick the location the list of sites appears
    if request.method == 'POST':
        sites_form = SelectWaterSampleSiteForm(request.POST)
        trip_date = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).endfieldtrip
        trip_date = trip_date.strftime('%Y%m%d')
        samplenames_curr = {}
        for key in request.POST.getlist('selected_sites'):
            current_site = Site.objects.get(idsite=key)

            sitecode = current_site.sitecode
            samplename = '%s %s' %(trip_date, sitecode)
            masterlist_input = Samplenamemasterlist(samplename=samplename,
                                                    sampletype=Sampletype.objects.get(sampletype='groundwater')).save()
            sampledetail_input = Groundwatersampledetails(samplename=Samplenamemasterlist.objects.get(samplename=samplename),
                                                          site=Site.objects.get(idsite=key),
                                                          idfieldtrip=Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"])).save()

            samplenames_curr[current_site.site] = samplename

        for key in request.POST.getlist('workers'):
            worker_input = Fieldteam(workername=Worker.objects.get(idworker=key),
                                     idfieldtrip=Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"])).save()
        request.session["samplenames_curr"] = samplenames_curr
        return HttpResponseRedirect('/enter-site-data/')
    else:
        fieldtrip = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"])
        filtered_sites = Site.objects.exclude(active=0).exclude(sitetype='cave room').filter(location=fieldtrip.location)
        # workers = Worker.objects.exclude(active=0).exclude(workertype='lab').exclude(workertype='supervisory')
        sites_form = SelectWaterSampleSiteForm(filtered_sites=filtered_sites)
        # worker_form = SelectteamForm(workers=workers)
    return render(request, 'new_fieldtrip_sites.html', {'sites_form': sites_form,
                                                        # 'worker_form': worker_form,
                                                        })

def next_site_data(request):
    idfieldtrip_curr = request.session["idfieldtrip_curr"]
    current_idx = request.session.get("current_sample_idx", 0)
    print(current_idx)
    print(len(request.session["samplenames_curr"]))
    if current_idx >= len(request.session["samplenames_curr"]):
        print("Deleting it!")
        del request.session["current_sample_idx"]
        return None
    key = sorted(request.session["samplenames_curr"])[current_idx]
    print(key)
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
    WatersampleinventoryFormset = formset_factory(WatersampleinventoryForm, extra=0)
    collectedsamples_formset = WatersampleinventoryFormset(initial = [
        srcat_initial,
        anions_initial,
        d18O_initial,
        dD_initial,
        alk_initial,
        d13C_initial
    ])

    if key  == 'Pool':
        return render(request, 'enter_site_data.html', {'watersamplename': samplename,
                                                        'collectedsamples_formset': collectedsamples_formset,
                                                        })
    else:
        start_trip = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).beginfieldtrip
        end_trip = Fieldtrip.objects.get(pk=request.session["idfieldtrip_curr"]).endfieldtrip
        if (start_trip.day == end_trip.day) and (start_trip.month == end_trip.month) and (start_trip.year == end_trip.year):
            trip_length_flag = 1
        else:
            trip_length_flag = 0
        trip_days = ((None, '------'),
                     (datetime.datetime(start_trip.year, start_trip.month, start_trip.day), 'Day 1'),
                     (datetime.datetime(end_trip.year, end_trip.month, end_trip.day), 'Day 2'))
        initial_bottle_weights = {'Stumpy': '102.3',
                                  'Stumpys Brother': '68.2',
                                  'Station 1': '35.9',
                                  'Station 2': '57.8',
                                  'Flatman': '101.8',
                                  'Trinity': '102.6',
                                }
        initialmass = initial_bottle_weights[key]
        platedeploy_prev = Platefielddata.objects.filter(site=site).order_by('-idplatefielddata')[0]
        tmp_form = CavedripwaterForm(watersamplename=samplename,
                                     initialmass=initialmass,
                                     day_choices=trip_days,
                                     trip_length_flag = trip_length_flag)
        platecollect_form = PlatecollectForm(instance=platedeploy_prev)
        platedeploy_form = PlatedeplyForm(site=site,
                                          idfieldtrip=idfieldtrip_curr)
        return render(request, 'enter_site_data.html', {'tmp_form': tmp_form,
                                                        'platecollect_form': platecollect_form,
                                                        'platedeploy_form': platedeploy_form,
                                                        'site': site,
                                                        'watersamplename': samplename,
                                                        'start_trip': start_trip,
                                                        'end_trip': end_trip,
                                                        'collectedsamples_formset': collectedsamples_formset,
                                                        'analysis_display': analysis_display,
                                                        })

def enter_site_data(request):
    if request.method == 'POST':
        bottle_down_day = datetime.datetime.strptime(request.POST.get('bottle_down_day'), '%Y-%m-%d %H:%M:%S')
        bottle_down_time = datetime.datetime.strptime(request.POST.get('bottle_down_time'), '%H:%M')
        bottle_down = datetime.datetime(bottle_down_day.year, bottle_down_day.month, bottle_down_day.day, bottle_down_time.hour, bottle_down_time.minute)
        bottle_up_day = datetime.datetime.strptime(request.POST.get('bottle_up_day'), '%Y-%m-%d %H:%M:%S')
        bottle_up_time = datetime.datetime.strptime(request.POST.get('bottle_up_time'), '%H:%M')
        bottle_up = datetime.datetime(bottle_up_day.year, bottle_up_day.month, bottle_up_day.day, bottle_up_time.hour, bottle_up_time.minute)
        dripcollection = Dripcollectionbottle(samplename=Samplenamemasterlist.objects.get(samplename=request.POST.get('watersamplename')),
                                              initialmass=request.POST.get('initialmass'),
                                              finalmass=request.POST.get('finalmass'),
                                              deploytime=bottle_down,
                                              collecttime=bottle_up).save()
        dripcount_day = datetime.datetime.strptime(request.POST.get('dripcount_day'), '%Y-%m-%d %H:%M:%S')
        dripcount_time = datetime.datetime.strptime(request.POST.get('dripcount_time'), '%H:%M')
        dripcount_datetime = datetime.datetime(dripcount_day.year, dripcount_day.month, dripcount_day.day, dripcount_time.hour, dripcount_time.minute)
        # dripinterval = Dripinterval(idfieldtrip=Fieldtrip.objects.get(idfieldtrip=request.session["idfieldtrip_curr"]),
        #                             site=Site.objects.get(site=))
        platecollect_form = PlatecollectForm(request.POST)
        platedeploy_form = PlatedeplyForm(request.POST)
        fieldchem_form = FieldwaterchemistryForm(request.POST)
        WatersampleinventoryFormset = formset_factory(WatersampleinventoryForm, extra=0)
        collectedsamples_formset = WatersampleinventoryFormset(request.POST)
        if tmp_form.is_valid():
            data = tmp_form.save()
        if dripinterval_form.is_valid():
            data = dripinterval_form.save()
        if platecollect_form.is_valid():
            data = platecollect_form.save()
        if platedeploy_form.is_valid():
            data = platedeploy_form.save()
        if fieldchem_form.is_valid():
            data = fieldchem_form.save()
        if collectedsamples_formset.is_valid():
            for form in collectedsamples_formset:
                form.save()
        next_site = next_site_data(request)
        if next_site:
            return next_site
        else:
            return HttpResponseRedirect('/samples-collected/')
    else:
        if request.session.get("current_sample_idx", None):
            del request.session["current_sample_idx"]

        next_site = next_site_data(request)
        if next_site:
            return next_site
        else:
            return HttpResponseRedirect('/errar/')

def alk(request):
    form = AlkalinityForm()
    return render(request, 'alk.html', {'form': form})

def enter_data(request):
    return render(request, 'enter_data.html',)

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
