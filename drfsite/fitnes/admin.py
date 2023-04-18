from django.contrib import admin

from .models import CatDirection, CatSession, CatCoach, Session

admin.site.register([
    CatDirection,
    CatSession,
    CatCoach,
    Session,
])
