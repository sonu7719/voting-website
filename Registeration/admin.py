from atexit import register
from django.contrib import admin

from Registeration.models import Register

# Register your models here.
admin.site.register(Register)
