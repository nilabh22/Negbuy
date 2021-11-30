from django.contrib import admin
from .models import *
# Register your models here.


class readFields(admin.ModelAdmin):
    readonly_fields = ('created_at', 'modified_at')


admin.site.register(procure_userdb, readFields)
