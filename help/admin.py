from django.contrib import admin

from .models import HelpItem, HelpSection


class HelpSectionAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content', 'title_ja', 'content_ja')
    list_display = ('title', 'sort')


class HelpItemAdmin(admin.ModelAdmin):
    raw_id_fields = ('section',)
    search_fields = ('title', 'content', 'title_ja', 'content_ja')
    list_display = ('title', 'section', 'sort')


admin.site.register(HelpSection, HelpSectionAdmin)
admin.site.register(HelpItem, HelpItemAdmin)
