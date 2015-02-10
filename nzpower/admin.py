from django.contrib import admin
from . import models as m

class CompanyAdmin(admin.ModelAdmin):
    model = m.Company
    list_display = ['name', 'slug', 'bank_account_no']

admin.site.register(m.Company, CompanyAdmin)

