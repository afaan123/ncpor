#Changed By Afaan
from django.contrib import admin
from nsidc_app.models import about
from django.contrib.auth.models import User
# from nsidc_app.models import research_drop

from nsidc_app.models import informationResearch

from nsidc_app.models import staff
from nsidc_app.models import vessel
from nsidc_app.models import rit
from nsidc_app.models import feedback

from nsidc_app.models import bytes

from nsidc_app.models import test1
from nsidc_app.models import test2

from nsidc_app.models import administrative
from nsidc_app.models import finance
from nsidc_app.models import procurement
from nsidc_app.models import e_state

from nsidc_app.models import bytes
from nsidc_app.models import readmore


from nsidc_app.models import gem,eprocurement,panelment
from nsidc_app.models import enquiry,corigendum
from nsidc_app.models import career

from nsidc_app.models import polarenvironments,polaroceans,polarscience,mineralresources,geosciences,atmosphere
from nsidc_app.models import  antarctic,arctic,southern_ocean,himalaya,new,event,data
# Register your models here.
from nsidc_app.models import get_help

from django.utils.html import format_html


class AdminDesign(admin.ModelAdmin): #Changes done by Afaan
    list_display = ('id','title', 'slug','is_featured')
    list_display_links =  ('id','title','slug')

    search_fields= ('title','slug')
    list_editable=('is_featured',)
    list_filter= ('title','slug',)
    css={
        "all":("css/main.css",)
    }
    js=("js/blog.js",)


class ClassAdminDesign(admin.ModelAdmin): #Changes done by Afaan
    list_display = ('id','slno','tenderno','description','releasedate','closingdate')
    list_display_links =  ('id','slno','tenderno')

    search_fields= ('id','slno','tenderno','description','releasedate','closingdate')
    list_filter= ('tenderno','releasedate','closingdate',)
    css={
        "all":("css/main.css",)
    }
    js=("js/blog.js",)


class newEventAdminDesign(admin.ModelAdmin): #Changes done by Afaan
    list_display = ('id','sno','description','closingdate','is_featured')
    list_display_links =  ('id','sno','description')

    search_fields= ('id','sno','description','closingdate')
    list_editable=('is_featured',)
    list_filter= ('description','closingdate',)

    css={
        "all":("css/main.css",)
    }
    js=("js/blog.js",)

class DataWebAdminDesign(admin.ModelAdmin): #Changes done by Afaan
    list_display = ('id','description','is_featured')
    list_display_links =  ('id','description')

    search_fields= ('id','description')
    list_editable=('is_featured',)
    list_filter= ('description',)
    css={
        "all":("css/main.css",)
    }
    js=("js/blog.js",)



class staffAdmin(admin.ModelAdmin):
        def thumbnail(self, object):
            return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.photo.url))

        thumbnail.short_description = 'staff Photo'

        list_display = ('id','thumbnail','name','designation','email_id','desk_no','is_featured')
        list_display_links=('id','thumbnail','name')

        list_editable=('is_featured',)
        search_fields=('name','designation','email_id','desk_no')

        list_filter=('name','designation','email_id','desk_no')

class RitAdmin(admin.ModelAdmin):

        list_display = ('sl_No','title','download','is_featured')
        list_display_links=('sl_No','title')
        search_fields=('sl_No','title')
        list_editable=('is_featured',)
        list_filter=('title',)


class ByteAdmin(admin.ModelAdmin):
        def thumbnail(self, object):
            return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.photo.url))

        thumbnail.short_description = 'Photo'
        list_display = ('title','thumbnail','is_featured')
        list_display_links=('title',)
        search_fields=('title',)
        list_editable=('is_featured',)
        list_filter=('title',)

class Finance_Administrative_ProcurementAdmin(admin.ModelAdmin):

        list_display = ('sl_No','name','designation','is_featured')
        list_display_links=('name','designation')
        search_fields=('name','designation')
        list_editable=('is_featured',)
        list_filter=('name','designation')

class estate(admin.ModelAdmin):

        list_display = ('sr_no','is_featured')
        list_display_links=('sr_no')
        list_editable=('is_featured',)





admin.site.register(administrative,Finance_Administrative_ProcurementAdmin)
admin.site.register(procurement,Finance_Administrative_ProcurementAdmin)
admin.site.register(e_state)
admin.site.register(finance,Finance_Administrative_ProcurementAdmin)



admin.site.register(feedback)
admin.site.register(vessel)
admin.site.register(rit,RitAdmin)
admin.site.register(bytes)
admin.site.register(readmore)

admin.site.register(staff,staffAdmin)


admin.site.register(about,AdminDesign)



admin.site.register(informationResearch, AdminDesign)



admin.site.register(antarctic,AdminDesign)
admin.site.register(arctic,AdminDesign)
admin.site.register(southern_ocean,AdminDesign)
admin.site.register(himalaya,AdminDesign)
admin.site.register(corigendum,ClassAdminDesign)
admin.site.register(panelment,ClassAdminDesign)
admin.site.register(eprocurement,ClassAdminDesign)
admin.site.register(gem,ClassAdminDesign)
admin.site.register(enquiry,ClassAdminDesign)
admin.site.register(career,ClassAdminDesign)
admin.site.register(polarenvironments,AdminDesign)
admin.site.register(polaroceans,AdminDesign)
admin.site.register(polarscience,AdminDesign)
admin.site.register(geosciences,AdminDesign)
admin.site.register(atmosphere,AdminDesign)
admin.site.register(mineralresources,AdminDesign)
admin.site.register(new,newEventAdminDesign)
admin.site.register(event,newEventAdminDesign)
admin.site.register(data,DataWebAdminDesign)

admin.site.register(get_help)


# admin.site.register(research_drop,BlogAdmin)(drop-dowm-->dropdowm through cms / made by priyanshi)
