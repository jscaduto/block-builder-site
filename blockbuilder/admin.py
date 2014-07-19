from django.contrib import admin
from blockbuilder.models import Phrase

class PhraseAdmin(admin.ModelAdmin):
    list_display = ('phrase_text', 'request_date', 'possible')

admin.site.register(Phrase, PhraseAdmin)