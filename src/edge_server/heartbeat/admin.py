from django.contrib import admin

from heartbeat.models import HeartBeat


@admin.register(HeartBeat)
class HeartBeatAdmin(admin.ModelAdmin):
    date_hierarchy = 'last_seen'
    list_display = ('service', 'last_seen')
    list_filter = ('service',)
