from django.contrib import admin
from . import models 

# Register your models here.
# admin.site.register(models.User)
@admin.register(models.User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    
    


