from django.contrib import admin
from .models import CustomUser, PGListing, Application
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(PGListing)
admin.site.register(Application)

