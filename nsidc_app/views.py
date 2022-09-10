from datetime import datetime
from http.client import HTTPResponse
from django.forms import DateField
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from nsidc_app.models import about
from nsidc_app.models import get_help

from django.utils import timezone

from nsidc_app.models import administrative
from nsidc_app.models import finance
from nsidc_app.models import procurement
from nsidc_app.models import e_state

from nsidc_app.models import readmore

from nsidc_app.models import staff
from nsidc_app.models import feedback
from nsidc_app.models import vessel
from nsidc_app.models import rit
from nsidc_app.models import bytes
from nsidc_app.models import informationResearch
from nsidc_app.models import gem,eprocurement,panelment
from nsidc_app.models import enquiry,corigendum
from nsidc_app.models import career
from nsidc_app.models import antarctic,arctic,southern_ocean,himalaya
from nsidc_app.models import polarenvironments,polaroceans,polarscience,mineralresources,geosciences,atmosphere,new,event,data
# Create your views here.

from nsidc_app.models import ict

from nsidc_app.models import staff




def home(request):
    featured_about = about.objects.filter(is_featured=True)
    abouts = about.objects.filter(is_featured=True)

    research_example_down_resgr = antarctic.objects.filter(is_featured=True)
    research_example_down_sps = arctic.objects.filter(is_featured=True)
    # researchs_drops = research_drop.objects.all()
    informationResearchs = informationResearch.objects.filter(is_featured=True)



    research_example_down_scientist = southern_ocean.objects.filter(is_featured=True)
    research_example_down = himalaya.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    news = new.objects.filter(is_featured=True)
    c = news.exclude(closingdate__lte=datetime.today())
    eve = event.objects.filter(is_featured=True)
    d = eve.exclude(closingdate__lte=datetime.today())
    datas = data.objects.filter(is_featured=True)
    prof=staff.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'pf':prof,'ab': abouts,'feature':featured_about, 'informationResearchs': informationResearchs,
                'redsc': research_example_down_scientist, 'redrg': research_example_down_resgr, "down_publ": research_example_down_sps, 'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,'him':research_example_down,'nw':c,'event':d,'data':datas,}
    return render(request, 'home.html', context)
# def about_jobs(request):
#     return HttpResponse("this is home page")
# def about_ncpor(request):
#     return HttpResponse("this is home page")
# def about_sponsors(request):
#     return HttpResponse("this is home page")
# def about_highlights(request):
#     return HttpResponse("this is home page")
# def about_copyright(request):
#     return HttpResponse("this is home page")
# def about_contact(request):
#     return HttpResponse("this is home page")
# def about_greendata(request):
#     return HttpResponse("this is home page")
# def about_home(request):
#     abouts = about.objects.all()
#     context = {'abouts':abouts}
#     return render(request,'about.html',context)

def vessel_example(request):
    abouts = about.objects.filter(is_featured=True)


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    vessels = vessel.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {
               've':vessels,
               'ab': abouts,


               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'researcher_vessel.html', context)


def read(request):
    re = readmore.objects.filter(is_featured=True)
    abouts = about.objects.filter(is_featured=True)
    rits = rit.objects.filter(is_featured=True)


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    vessels = vessel.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    context = {
               'r':re,
               're':rits,
               've':vessels,
               'ab': abouts,


               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'readmore.html', context)


def rit_example(request):
    abouts = about.objects.filter(is_featured=True)
    rits = rit.objects.filter(is_featured=True)


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    vessels = vessel.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)

    # web = webmail.objects.all()
    context = {
               're':rits,
               've':vessels,
               'ab': abouts,


               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'rit.html', context)


def byte_example(request):
    abouts = about.objects.filter(is_featured=True)
    rits = rit.objects.filter(is_featured=True)


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    vessels = vessel.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    by = bytes.objects.filter(is_featured=True)
    bt = bytes.objects.filter(is_featured=True)

    if 'gallery' in request.GET:
        gallery = request.GET['gallery']
        if gallery:
            by = by.filter(title__iexact=gallery)

    context = {
               'bi':bt,
               'be':by,
               're':rits,
               've':vessels,
               'ab': abouts,


               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'byte.html', context)




def feedback_example(request):
    if request.method == 'POST':
        content = request.POST['feedback']
        feedbacks = feedback(content=content)
        feedbacks.save()
    return render(request, 'feedback.html')


def administrative_example(request):
    abouts = about.objects.filter(is_featured=True)
    administratives = administrative.objects.filter(is_featured=True)


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'ad':administratives,

               'ab': abouts,


               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'administrative.html', context)


def finance_example(request):
    abouts = about.objects.filter(is_featured=True)
    finances = finance.objects.filter(is_featured=True)



    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'fn':finances,

               'ab': abouts,



               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'finance.html', context)

def procurement_example(request):
    abouts = about.objects.filter(is_featured=True)
    procurements = procurement.objects.filter(is_featured=True)


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'pr':procurements,

               'ab': abouts,


               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'procurement.html', context)


def estate_example(request):
    abouts = about.objects.filter(is_featured=True)
    estates = e_state.objects.filter(is_featured=True)



    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'es':estates,
               'ab': abouts,
               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'estate.html', context)




def about_example(request, slug):
    abouts = about.objects.filter(is_featured=True)

    About = about.objects.filter(slug=slug).first()


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'about': About,
               'ab': abouts,



               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'about.html', context)




def expendition_example(request, slug):
    abouts = about.objects.filter(is_featured=True)

    Expendition = expendition.objects.filter(slug=slug).first()

    About = about.objects.filter(slug=slug).first()


    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'about': About,
               'expendition':Expendition,
               'ab': abouts,




               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'expendition.html', context)






def get_help_example(request, slug):
    abouts = about.objects.filter(is_featured=True)

    About = about.objects.filter(slug=slug).first()


    get_helps= get_help.objects.filter(is_featured=True)
    Get_help = get_help.objects.filter(slug=slug).first()

    informationResearchs =informationResearch.objects.filter(is_featured=True)
    InformationResearch = informationResearch.objects.filter(slug=slug).first()

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'about': About,
               'ab': abouts,

               'ge': Get_help,



               'ifrsc': InformationResearch,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'get_help.html', context)


def informationResearch_example(request, slug):
    abouts = about.objects.filter(is_featured=True)

    About = about.objects.filter(slug=slug).first()

    get_helps= get_help.objects.filter(is_featured=True)
    Get_help = get_help.objects.filter(slug=slug).first()

    informationResearchs = informationResearch.objects.filter(is_featured=True)
    InformationResearch = informationResearch.objects.filter(slug=slug).first()

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'about': About,
               'ab': abouts,

               'ge': Get_help,



               'ifrsc': InformationResearch,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'information_research.html', context)



def information_example(request, slug):
    abouts = about.objects.filter(is_featured=True)

    About = about.objects.filter(slug=slug).first()


    get_helps= get_help.objects.filter(is_featured=True)
    Get_help = get_help.objects.filter(slug=slug).first()

    informationResearchs = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.filter(is_featured=True)
    polarenv = polarenvironments.objects.filter(is_featured=True)
    polaroc = polaroceans.objects.filter(is_featured=True)
    polarsc = polarscience.objects.filter(is_featured=True)
    minre = mineralresources.objects.filter(is_featured=True)
    geosc = geosciences.objects.filter(is_featured=True)
    atm = atmosphere.objects.filter(is_featured=True)
    # web = webmail.objects.all()
    context = {'about': About,
               'ab': abouts,

               'ge': Get_help,



               'ifrsc': informationResearchs,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'get_help.html', context)



# Research
def research_scientists(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'research/r_scientists.html', context)


def research_grants(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'research/research_grants.html', context)


def research_publications(request):
    abouts = about.objects.filter(is_featured=True)


    researchPublications = scientificPublication.objects.filter(is_featured=True)
    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'research/scientific_publications.html', context)


def research_information(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.filter(is_featured=True)

    datas= data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'research/InformationResearch.html', context)


def scientific_expeditions(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'research/ScientificExpeditions.html', context)


# def research_example(request,slug):
#     Researchs = research.objects.filter(slug=slug).first()
#     context = {'research':Researchs}
#     return render(request,'research_example.html',context)
def research_scientists_example(request, slug):
    abouts = about.objects.filter(is_featured=True)
    Researchs = antarctic.objects.filter(slug=slug).first()



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {'research': Researchs,
               'ab': abouts,



               'ri': researchInformation,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'research/research_scientist_example.html', context)


def research_grants_example(request, slug):
    abouts = about.objects.filter(is_featured=True)
    Researchs = arctic.objects.filter(slug=slug).first()



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {'research': Researchs,
               'ab': abouts,



               'ri': researchInformation,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'research/research_grant_example.html', context)


def research_publications_example(request, slug):
    abouts = about.objects.filter(is_featured=True)
    Researchs = southern_ocean.objects.filter(slug=slug).first()



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {'research': Researchs,
               'ab': abouts,



               'ri': researchInformation,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc,
               }
    return render(request, 'research/research_publications_example.html', context)


def research_information_example(request, slug):
    abouts = about.objects.filter(is_featured=True)
    Researchs = himalaya.objects.filter(slug=slug).first()



    researchInformation = informationResearch.objects.filter(is_featured=True)

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {'research': Researchs,
               'ab': abouts,



               'ri': researchInformation,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'research/research_IR_example.html', context)


def scientific_expeditions_example(request, slug):
    abouts = about.objects.filter(is_featured=True)
    Researchs = himalaya.objects.filter(slug=slug).first()



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {'research': Researchs,
               'ab': abouts,



               'ri': researchInformation,

               'data': datas,
               'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
               }
    return render(request, 'research/research_scientific_example.html', context)


# image Dropdown
def Antarctic(request, slug):
    rsres = antarctic.objects.filter(slug=slug).first()
    rsres= rsres.filter(is_featured=True)
    context = {'resrchesg': rsres}
    return render(request, 'research/research_example.html', context)


def Arctic(request, slug):
    rsres = arctic.objects.filter(slug=slug).first()
    rsres= rsres.filter(is_featured=True)
    context = {'resrchesg': rsres}
    return render(request, 'research/research_example.html', context)


def Southern_ocean(request, slug):
    resgr = southern_ocean.objects.filter(slug=slug).first()
    resgr= resgr.filter(is_featured=True)
    context = {'resrchesg': resgr}
    return render(request, 'research/research_example.html', context)


def Himalaya(request, slug):
    publica = himalaya.objects.filter(slug=slug).first()
    publica= publica.filter(is_featured=True)
    context = {'resrchesg': publica}
    return render(request, 'research/research_example.html', context)
    # return render(request,'research/research_scientific_example.html',context)
    # return HttpResponse("fbjfns")

# def research_drop_example(request,slug,slug_drop):
#     Researchs_Drops = research_drop.objects.filter(slug=slug,slug_drop=slug_drop).first()
#     context = {'research_drop':Researchs_Drops}
#     return render(request,'research_drop.html',context)(drop-dowm-->dropdowm through cms / made by priyanshi)

def tender(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'tender.html', context)
    # return HttpResponse("hello")


def tenderTable(request):

    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'co':cd,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/tenderTable.html", context)

def CorrigendumTable(request):
    c=corigendum.objects.filter(is_featured=True)
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'c':c,
        'co':cd,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/CorrigendumTable.html", context)

    # return HttpResponse("fnfjn")
def ProcurementTable(request):
    c=eprocurement.objects.filter(is_featured=True)
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.filter(is_featured=True)

    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'co':c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/ProcurementTable.html", context)
def PanelmentTable(request):
    c=panelment.objects.filter(is_featured=True)
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'c':c,
        'co':cd,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/PanelmentTable.html", context)
def EnquiryTable(request):
    c=enquiry.objects.filter(is_featured=True)
    cd=c.exclude(closingdate__lte=datetime.today())

    abouts =about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'co':c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/EnquiryTable.html", context)
def GeMTable(request):
    c=gem.objects.filter(is_featured=True)
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'c':c,
        'co':cd,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/GeMTable.html", context)

def tenderArchive(request):

    c1=corigendum.objects.filter(is_featured=True)
    c2=panelment.objects.filter(is_featured=True)
    c3=eprocurement.objects.filter(is_featured=True)
    c4=gem.objects.filter(is_featured=True)
    c5 = enquiry.objects.filter(is_featured=True)
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c1 = c1.filter(releasedate__icontains=year)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c2 = c2.filter(releasedate__icontains=year)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c3 = c3.filter(releasedate__icontains=year)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c4 = c4.filter(releasedate__icontains=year)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c5 = c5.filter(releasedate__icontains=year)



    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if year:
            c1 = c1.filter(description__icontains=keyword)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if year:
            c2 = c2.filter(description__icontains=keyword)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            c3 = c3.filter(description__icontains=keyword)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            c4 = c4.filter(description__icontains=keyword)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            c5 = c5.filter(description__icontains=keyword)


    context = {
        'co1':c1,
        'co2':c2,
        'co3':c3,
        'co4':c4,
        'co5':c5,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "tender/tenderArchive.html", context)


# career
def careers(request):
    c=career.objects.filter(is_featured=True)
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts =about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'co':cd,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "career.html", context)

def profiles(request):
    prof=staff.objects.filter(is_featured=True)
    abouts=about.objects.filter(is_featured=True)
    datas=data.objects.filter(is_featured=True)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            prof = prof.filter(name__icontains=keyword)

    if 'designation' in request.GET:
        designation = request.GET['designation']
        if designation:
            prof = prof.filter(designation__iexact=designation)


    context = {'prof': prof,
    'data': datas,
    'ab': abouts,}
    return render(request, 'profiles.html',context)

def single_profile(request, id):
    single_prof = get_object_or_404(staff, pk=id)
    abouts=about.objects.filter(is_featured=True)
    datas=data.objects.filter(is_featured=True)

    context = {
        'sf': single_prof,
'data': datas,
'ab': abouts,}
    return render(request, 'ncpor_profiles.html', context)


def careerArchive(request):
    c = career.objects.filter(is_featured=True)
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c = c.filter(releasedate__icontains=year)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            c = c.filter(description__icontains=keyword)

    context = {
        'co':c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "careerArchive.html", context)

# Webmail

def news(request):
    abouts =about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, "news.html", context)


# our research drop down

def polar_science(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    polar_res = polarscience.objects.filter(slug=slug).first()
    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,


        'ri': researchInformation,

        'po': polar_res,
        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'our_research/polarscience.html', context)

def polar_oceans(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    polar_res = polaroceans.objects.filter(slug=slug).first()
    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'po': polar_res,
        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'our_research/polaroceans.html', context)

def polar_env(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    polar_res = polarenvironments.objects.filter(slug=slug).first()
    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'po': polar_res,
        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'our_research/polarenv.html', context)

def mineral_resources(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    polar_res = mineralresources.objects.filter(slug=slug).first()
    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'po': polar_res,
        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'our_research/mineralresources.html', context)

def atmos(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    polar_res = atmosphere.objects.filter(slug=slug).first()
    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'po': polar_res,
        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'our_research/atmos.html', context)

def geoscience(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    polar_res = geosciences.objects.filter(slug=slug).first()
    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'po': polar_res,
        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'our_research/geoscience.html', context)

def dataCenter(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    context = {
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'DataCenter.html', context)

# news and event

def news_archive(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    c = new.objects.filter(closingdate__lte=datetime.today())
    c= c.filter(is_featured=True)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c = c.filter(closingdate__icontains=year)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            c = c.filter(description__icontains=keyword)

    context = {
        'co' : c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
    }
    return render(request, 'news_archive.html',context)

def event_archive(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()

    c = event.objects.filter(closingdate__lte=datetime.today())
    c= c.filter(is_featured=True)


    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            c = c.filter(closingdate__icontains=year)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            c = c.filter(description__icontains=keyword)

    context = {
        'co' : c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm
    }
    return render(request, 'events_archive.html',context)

def data_centre(request,slug):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    d = data.objects.filter(slug=slug).first()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    # web = webmail.objects.all()
    c = event.objects.filter(closingdate__lte=datetime.today())
    context = {
        'co' : c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
        'd':d
    }
    return render(request, 'data_class.html',context)

def mineral(request):
    abouts = about.objects.filter(is_featured=True)



    researchInformation = informationResearch.objects.all()

    datas = data.objects.all()
    d = data.objects.all()
    polarenv = polarenvironments.objects.all()
    polaroc = polaroceans.objects.all()
    polarsc = polarscience.objects.all()
    minre = mineralresources.objects.all()
    geosc = geosciences.objects.all()
    atm = atmosphere.objects.all()
    c = event.objects.filter(closingdate__lte=datetime.today())
    # we = webmail.objects.filter(slug=slug).first()
    context = {
        'co' : c,
        'ab': abouts,



        'ri': researchInformation,

        'data': datas,
        'polen':polarenv, 'poloc':polaroc, 'polsc':polarsc, 'mre':minre, 'gsc':geosc, 'am':atm,
        'd':d
    }
    return render(request, 'research/mineral.html',context)
