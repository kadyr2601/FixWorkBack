from django.contrib import admin
from restoration_page import models


admin.site.register(models.FAQ)

class RestorationServiceInline(admin.StackedInline):
    model = models.RestorationService
    extra = 1


@admin.register(models.Restoration)
class RestorationAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [RestorationServiceInline,]