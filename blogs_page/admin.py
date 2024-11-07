from django.contrib import admin
from . import models


admin.site.register(models.SingleBannerImage)
admin.site.register(models.SingleBannerVideo)
admin.site.register(models.ServiceCard)
admin.site.register(models.BlogsPage)
admin.site.register(models.MainBanner)

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
