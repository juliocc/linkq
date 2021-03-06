from django.contrib import admin
from .models import Link

class LinkAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('title', 'url', 'created', 'read')

admin.site.register(Link, LinkAdmin)

