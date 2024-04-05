from django.contrib import admin

from result.models import  vote, cal_votes

# Register your models here.
admin.site.register(vote)
admin.site.register(cal_votes)
