from django.contrib import admin
from .models import ComputerScienceModel


# Register your models here.
class ComputerScienceAdmin(admin.ModelAdmin):
    list_display = ['Name','Age','Email','Mobile']

admin.site.register(ComputerScienceModel,ComputerScienceAdmin)