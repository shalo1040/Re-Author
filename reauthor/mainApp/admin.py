from django.contrib import admin
from .models import Profile, Toon, Restory, Characters, CharactersPosition

admin.site.register(Profile)
admin.site.register(Toon)
admin.site.register(Restory)
admin.site.register(Characters)
admin.site.register(CharactersPosition)