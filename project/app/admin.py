from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Gallary)

@admin.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Price','ColorName']


@admin.register(Transactions)

class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['user']


# register session
from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)