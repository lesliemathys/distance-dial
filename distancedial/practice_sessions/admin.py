from django.contrib import admin
from .models import Session, Shot

class ShotInline(admin.TabularInline):
    model = Shot
    extra = 1
    fields = ('club', 'distance', 'timestamp', 'is_deleted')
    readonly_fields = ('timestamp',)

    def get_queryset(self, request):
        # Show all shots, including soft-deleted ones
        return self.model.all_objects.all()

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_datetime', 'get_shot_count', 'session_notes', 'is_deleted')
    list_filter = ('user', 'session_datetime', 'is_deleted')
    search_fields = ('user__email', 'session_notes')
    date_hierarchy = 'session_datetime'
    inlines = [ShotInline]
    list_per_page = 25

    def get_shot_count(self, obj):
        """Return number of shots in session"""
        return obj.shot_set.count()
    get_shot_count.short_description = 'Shots'

    def get_queryset(self, request):
        # Show all sessions, including soft-deleted ones
        return self.model.all_objects.all()

@admin.register(Shot)
class ShotAdmin(admin.ModelAdmin):
    list_display = ('session', 'club', 'distance', 'timestamp', 'is_deleted')
    list_filter = ('club', 'session__user', 'timestamp', 'is_deleted')
    search_fields = ('session__user__email',)
    date_hierarchy = 'timestamp'
    list_per_page = 25

    def get_queryset(self, request):
        # Show all shots, including soft-deleted ones
        return self.model.all_objects.all()