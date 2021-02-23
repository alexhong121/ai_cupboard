from django.contrib import admin
from users.models import Questions,Profiles,Departments,Quest_answers

# Register your models here.
admin.site.register(Questions)
admin.site.register(Profiles)
admin.site.register(Departments)
admin.site.register(Quest_answers)