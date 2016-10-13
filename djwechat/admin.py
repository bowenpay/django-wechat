from django.contrib import admin
from djwechat.models import Config


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('kind', 'value')

admin.site.register(Config, ConfigAdmin)
