from django.contrib import admin
from site_setup.models import MenuLink

@admin.register(MenuLink)
class MenulinkAdmin(admin.ModelAdmin):
    list_display = 'id','text', 'url_or_path',
    list_display_links = 'id','text', 'url_or_path',
    search_fiels = 'id','text', 'url_or_path',