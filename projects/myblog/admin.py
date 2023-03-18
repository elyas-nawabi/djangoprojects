from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(Message)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']
