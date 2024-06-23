from django.contrib import admin
from .models import *


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['phone_number']


@admin.register(Reasons)
class ReasonsAdmin(admin.ModelAdmin):
    list_display = ['reason_text']


@admin.register(Calls)
class CallsAdmin(admin.ModelAdmin):
    list_display = ['cmr_id', 'call_date', 'issue_resolved']


@admin.register(Call_Reasons)
class CallReasonsAdmin(admin.ModelAdmin):
    list_display = ['cl_id', 'reason_id']


@admin.register(Resolutions)
class ResolutionsAdmin(admin.ModelAdmin):
    list_display = ['cl_id', 'resolution_text']