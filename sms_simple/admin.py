from django.contrib import admin
from .models import AfricasTalking, AfricasTalkingTestReceivers


class AdminAfricasTalking(admin.ModelAdmin):
    list_display = ('__str__', )
    fieldsets = (
        (None, {'fields': ('username', )}),
        ('Configurations', {'fields': ('api_key', 'secret_key', 'default')}),
    )


admin.site.register(AfricasTalking, AdminAfricasTalking)
admin.site.register(AfricasTalkingTestReceivers)