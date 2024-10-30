from django.contrib import admin
from .models import Session, Shot

class ShotInline(admin.TabularInline):
    model = Shot
    extra = 1  # Number of empty forms to display
    fields = ('club', 'distance', 'timestamp')
    readonly_fields = ('timestamp',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_datetime', 'get_shot_count', 'session_notes')
    list_filter = ('user', 'session_datetime')
    search_fields = ('user__email', 'session_notes')
    date_hierarchy = 'session_datetime'
    inlines = [ShotInline]

    def get_shot_count(self, obj):
        """Return number of shots in session"""
        return obj.shot_set.count()
    get_shot_count.short_description = 'Shots'

@admin.register(Shot)
class ShotAdmin(admin.ModelAdmin):
    list_display = ('session', 'club', 'distance', 'timestamp')
    list_filter = ('club', 'session__user', 'timestamp')
    search_fields = ('session__user__email',)
    date_hierarchy = 'timestamp'