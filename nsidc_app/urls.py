from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home , name= 'home'),

    path("profiles", views.profiles , name= 'profiles'),
    path('<int:id>', views.single_profile, name='single_profile'),
    path("vessel_example", views.vessel_example , name= 'vessel_example'),

    path("rit_example", views.rit_example , name= 'rit_example'),

    path("read", views.read , name= 'read'),

    path("byte_example", views.byte_example , name= 'byte_example'),

    path("feedback_example", views.feedback_example , name= 'feedback_example'),

    path("administrative_example", views.administrative_example , name= 'administrative_example'),
    path("procurement_example", views.procurement_example , name= 'procurement_example'),
    path("finance_example", views.finance_example , name= 'finance_example'),
    path("estate_example", views.estate_example , name= 'estate_example'),


    # path("about/", views.about_home , name= 'about'),
    # path("about/jobs", views.about_jobs , name= 'about'),
    # path("about/contact", views.about_contact , name= 'about'),
    # path("about/copyright", views.about_copyright , name= 'about'),
    # path("about/greendata", views.about_greendata , name= 'about'),
    # path("about/highlights", views.about_highlights , name= 'about'),
    # path("about/ncpor", views.about_ncpor , name= 'about'),
    # path("about/sponsors", views.about_sponsors , name= 'about'),
    path("about_example/<str:slug>",views.about_example,name = 'example'),

    path("expendition_example/<str:slug>",views.expendition_example,name = 'expendition_example'),

    path("get_help_example/<str:slug>",views.get_help_example,name = 'get_help_example'),

    path("informationResearch_example/<str:slug>",views.informationResearch_example,name = 'informationResearch_example'),


    path("research/information", views.research_information , name= 'research'),
    path("research/publications", views.research_publications , name= 'research'),
    path("research/research", views.research_grants , name= 'research'),
    path("research/scientists", views.research_scientists , name= 'research'),
    path("research/scientific", views.scientific_expeditions , name= 'research'),
    # path("research_example/<str:slug>",views.research_scientist_example,name = 'research_example'),
    path("research_information_example/<str:slug>",views.research_information_example,name = 'research_example'),


    path("research_publications_example/<str:slug>",views.research_publications_example,name = 'research_example'),
    path("research_grants_example/<str:slug>",views.research_grants_example,name = 'research_example'),
    path("research_scientist_example/<str:slug>",views.research_scientists_example,name = 'research_example'),

    path("scientific_expeditions_example/<str:slug>",views.scientific_expeditions_example,name = 'research_example'),

    # path("research_example",views.research_example,name = 'research_example'),
    # path("research_example/research_scientists",views.res_exam_rese_sct,name="research"),
    path("research/research_example/<str:slug>",views.Antarctic,name = 'research_example'),

    path("research/research_grants/<str:slug>",views.Arctic,name = 'research_example'),
    path("research/research_down_publi/<str:slug>",views.Southern_ocean,name = 'research_example'),
    path("research/research_down_publi/<str:slug>",views.Himalaya,name = 'research_example'),
    path("tender/", views.tender, name="tender"),
    path("careers", views.careers, name="career"),
    path("careerArchive", views.careerArchive, name="career"),

    path("tender/tender", views.tenderTable, name="Tendor"),
    path("tender/corrigendum", views.CorrigendumTable, name="Tender"),
    path("tender/procurement", views.ProcurementTable, name="Tender"),
    path("tender/empanelment", views.PanelmentTable, name="Tender"),
    path("tender/enquiry", views.EnquiryTable, name="Tender"),
    path("tender/GeM", views.GeMTable, name="Tender"),
    path("tender/archive", views.tenderArchive, name="tenderArchive"),

    path("news", views.news, name="news"),

    path("polarscience/<str:slug>",views.polar_science,name= 'our_research'),
    path("atmosphere/<str:slug>",views.atmos,name= 'our_research'),
    path("geoscience/<str:slug>",views.geoscience,name= 'our_research'),
    path("polaroceans/<str:slug>",views.polar_oceans,name= 'our_research'),
    path("polarenv/<str:slug>",views.polar_env,name= 'our_research'),
    path("mineral/<str:slug>",views.mineral_resources,name= 'our_research'),

    path("dataCenter",views.dataCenter,name= 'dataCenter'),
    path("newsarchive",views.news_archive,name='news'),
    path("eventsarchive",views.event_archive,name='event'),

    path("datacentre/<str:slug>",views.data_centre,name= 'datacentre'),

    path('mineral',views.mineral,name='mineral'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
