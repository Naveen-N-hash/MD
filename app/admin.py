from django.contrib import admin

# Register your models here
from .models import Movies, Tvshows1, Seasons, Episodes, Category

admin.site.register(Movies)
admin.site.register(Tvshows1)
admin.site.register(Seasons)
admin.site.register(Episodes)
admin.site.register(Category)
