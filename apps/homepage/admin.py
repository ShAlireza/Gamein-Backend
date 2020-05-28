from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'team', 'role', 'picture', 'show_linked_in_url')
    list_display_links = ('last_name', )
    list_editable = ('team',)
    list_filter = ('team', 'role')
    search_fields = ['last_name', 'name', 'team', 'role']

    def show_linked_in_url(self, obj):
        return format_html('<a href="%s">%s</a>' % (obj.linked_in_url, obj.name + "'s LinkedIn"))
    show_linked_in_url.allow_tags = True
    show_linked_in_url.short_description = 'Linked-In'


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sponsor_class', 'picture', 'show_website')
    list_editable = ('sponsor_class',)
    def show_website(self, obj):
        return format_html('<a href="%s">%s</a>' % (obj.site_url, obj.name + "'s Website"))
    show_website.allow_tags = True
    show_website.short_description = 'Website'
    list_filter = ['sponsor_class']
    search_fields = ['name']


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'award')
    list_display_links = ('title',)
    list_editable = ('award', )
    search_fields = ['title']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quoter', 'context')
    search_fields = ['quoter', 'context']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'persian_date', 'date')
    list_display_links = ('title', )
    list_editable = ('persian_date', 'date')
    search_fields = ['title']


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'stat', 'icon')
    list_editable = ('icon', )
    search_fields = ['title']
