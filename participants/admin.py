from django.contrib import admin
from participants.models import Participant

# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'id')
    search_fields = ('name', 'id')


admin.site.register(Participant, ParticipantAdmin)
