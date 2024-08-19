from django.contrib import admin
from .models import Payment
from import_export.admin import ImportExportModelAdmin

@admin.register(Payment)
class Payment_Admin(ImportExportModelAdmin):
    # readonly_fields = ['amount', ]
    list_display = ['student', 'amount']
    list_display_links = ['student', 'amount']
    search_fields = ['student', 'group']
    ordering = ['student',]
