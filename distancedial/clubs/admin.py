from django.contrib import admin
from .models import Club, Bag

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('get_club_name', 'club_type')
    list_filter = ('club_type',)
    search_fields = ('club_type',)
    ordering = ('club_type',)
    list_per_page = 25


    def get_club_name(self, obj):
        """Return the full name of the club from CLUB_CHOICES"""
        return dict(Club.CLUB_CHOICES).get(obj.club_type)
    get_club_name.short_description = 'Club Name'

@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_club_count', 'is_deleted')
    list_filter = ('is_deleted',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    filter_horizontal = ('clubs',)
    list_per_page = 25

    def get_club_count(self, obj):
        """Return number of clubs in the bag"""
        return obj.clubs.count()
    get_club_count.short_description = 'Number of Clubs'

    def get_queryset(self, request):
        # Show all bags, including soft-deleted ones
        return self.model.all_objects.all()