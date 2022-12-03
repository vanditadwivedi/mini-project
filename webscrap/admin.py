from django.contrib import admin

# Register your models here.
from . models import jobDetails, Tags,Personalize
admin.site.register(jobDetails)
admin.site.register(Tags)
admin.site.register(Personalize)
