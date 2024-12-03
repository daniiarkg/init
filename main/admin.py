from django.contrib import admin
from .models import *
from random import choice, randint
from django.utils.html import format_html

def photo_report():
    return True

class ReportInline(admin.StackedInline):
    model = Report
    extra = 0
    readonly_fields = ['img_out']

    @admin.display(description='Просмотр фотографии')
    def img_out(self,obj):
        return format_html(f'<img src="/media/{obj.photo}" width="250" />')

class ReportAdmin(admin.ModelAdmin):
    list_display = ['date', 'plant']

    def save_model(self, request, obj, form, change):
        try:    
            obj.status = choice(STATUS_CHOICES)
        except:
            pass
        super().save_model(request, obj, form, change) 

class PlantAdmin(admin.ModelAdmin):
    readonly_fields = ['img_out']
    list_display = ['name', 'id', 'type']
    inlines = [ReportInline]
    
    @admin.display(description='Просмотр фотографии')
    def img_out(self,obj):
        return format_html(f'<img src="/media/{obj.photo}" width="250" />')

    def save_formset(self, request, obj, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
                # instance.photo = photo_report()
            instance.humidity = randint(50,80)
            instance.status = STATUS_CHOICES[0][0]
            instance.save()
            formset.save_m2m()

        formset.save()


# Register your models here.
admin.site.register(Plant, PlantAdmin)
# admin.site.register(Report, ReportAdmin)