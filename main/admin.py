from django.contrib import admin
from .models import *
from random import choice

def photo_report():
    return True

class ReportInline(admin.StackedInline):
    model = Report
    extra = 0

class ReportAdmin(admin.ModelAdmin):
    list_display = ['date', 'plant']

    def save_model(self, request, obj, form, change):
        try:    
            obj.status = choice(STATUS_CHOICES)
        except:
            pass
        super().save_model(request, obj, form, change) 

class PlantAdmin(admin.ModelAdmin):

    list_display = ['name', 'id', 'type']
    inlines = [ReportInline]
    def save_formset(self, request, obj, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
                # instance.photo = photo_report
            instance.status = choice(STATUS_CHOICES)[0]
            instance.save()
            formset.save_m2m()

        formset.save()


# Register your models here.
admin.site.register(Plant, PlantAdmin)
# admin.site.register(Report, ReportAdmin)