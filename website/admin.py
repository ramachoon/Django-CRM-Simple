from django.contrib import admin
from website.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone",)
