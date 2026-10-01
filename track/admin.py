from django.contrib import admin
from .models import track
# Register your models here.
@admin.register(track)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'description', 'amount')
    search_field = ('created_at',)
