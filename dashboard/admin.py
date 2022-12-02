from django.contrib import admin
from dashboard import models

class CountryDataAdmin(admin.ModelAdmin):
    fieldsets=[
        ('나라',{'fields': ['country']}),
        ('인구',{'fields': ['population']})
    ]
    list_display = ('country','population')
# Register your models here.
admin.site.register(models.CountryData,CountryDataAdmin)