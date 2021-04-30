from django.contrib import admin

# Register your models here.
from djob_data.models import JobTitle, City

class CiyAdmin(admin.ModelAdmin):
    search_fields = ('city',)

models = [JobTitle, City]

admin.site.register(models, CiyAdmin)