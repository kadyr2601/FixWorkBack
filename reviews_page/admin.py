from django.contrib import admin
from . import models

admin.site.register(models.Review)
admin.site.register(models.ReviewsPage)
admin.site.register(models.SingleBannerImage)
admin.site.register(models.SingleBannerVideo)
admin.site.register(models.ServiceCard)
admin.site.register(models.MainBanner)