from django.contrib import admin
from access.models import Locker_access,UI_access,Functions

# Register your models here.
class UI_accessAdmin(admin.ModelAdmin):
    list_display=(
      'name', 
    'Profiles_id',
    'Functions_id',
    'perm_read',
    'perm_unlink',
    'perm_write',
    'perm_create'
    )

class FunctionsAdmin(admin.ModelAdmin):
    list_display=(
        'active', 
        'name'
    )
admin.site.register(Locker_access)
admin.site.register(UI_access,UI_accessAdmin)
admin.site.register(Functions,FunctionsAdmin)
