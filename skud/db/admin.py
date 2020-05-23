from django.contrib import admin
from .models import Department, Worker, Client, AccessRights, Report


class NAdmin(admin.ModelAdmin):
    search_fields = ('fio',)

class ARAdmin(admin.ModelAdmin):

    list_filter = ('department__name',)
    search_fields = ('client__fio',)

admin.site.register(Department)
admin.site.register(Worker)
admin.site.register(Client, NAdmin)
admin.site.register(AccessRights, ARAdmin)
admin.site.register(Report)