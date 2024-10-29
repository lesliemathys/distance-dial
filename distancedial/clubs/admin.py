from django.contrib import admin
from .models import Club
from .models import Bag

# Register your models here.
admin.site.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('get_club_name', 'club_type')
    list_filter = ('club_type',)
    search_fields = ('club_type',)
    ordering = ('club_type',)

    def get_club_name(self, obj):
        """Return the full name of the club from CLUB_CHOICES"""
        return dict(Club.CLUB_CHOICES).get(obj.club_type)
    get_club_name.short_description = 'Club Name'  # Column header in admin

admin.site.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_club_count')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    filter_horizontal = ('clubs',)  # Makes club selection easier

    def get_clubs_list(self, obj):
        """Return a comma-separated list of clubs in the bag"""
        return ', '.join([str(club) for club in obj.clubs.all().order_by('club_type')])
    get_clubs_list.short_description = 'Clubs'
