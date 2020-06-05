from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'team', 'role', 'picture', 'linked_in_url')
    list_display_links = ('last_name', )
    list_editable = ('team','picture', 'linked_in_url')
    list_filter = ('team', 'role')
    search_fields = ['last_name', 'name', 'team', 'role']



@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sponsor_class', 'picture', 'show_website')
    list_editable = ('sponsor_class',)
    def show_website(self, obj):
        if obj.site_url:
            return format_html('<a href="%s">%s</a>' % (obj.site_url, obj.name + "'s Website"))
        else:
            return ''
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


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon')
    list_editable = ('url', 'icon')
    search_fields = ['name']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'context']
    list_editable = ('context',)
    search_fields = ['title']


@admin.register(StaffTeam)
class StaffTeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'head']
    list_display_links = ['team_name']
    search_fields = ['team_name', 'head',]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video']
    search_fields = ['title']
    list_editable = ['video']