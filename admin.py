from django.contrib import admin
from .models import AfricasTalking


class AdminAfricasTalking(admin.ModelAdmin):
    list_display = ('__str__', )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Configurations', {'fields': ('api_key', 'secret_key')}),
    )


admin.site.register(AfricasTalking, AdminAfricasTalking)