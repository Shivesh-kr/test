from django.contrib import admin
from .models import Station, Crime

# Register your models here.
admin.site.site_header = "Crime Prediction"
admin.site.site_title = "Crime Predition"


class CrimeAdmin(admin.ModelAdmin):
     list_display = ['reported_by', 'reported_on',
                     'station', 'description', 'type', 'reviewd']
     list_filter = ['reported_on', 'station', 'type', 'reviewd']
     list_editable = ['reviewd']

admin.site.register(Crime, CrimeAdmin)

class StationAdmin(admin.ModelAdmin):
     list_display = ['title', 'location', 'pincode', 'incharge', 'contact']
     list_filter = ['location', 'pincode']

admin.site.register(Station, StationAdmin)
