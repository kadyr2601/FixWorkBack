from django.contrib import admin
from . import models


class ProjectSectionInline(admin.StackedInline):
    model = models.ProjectSection
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectSectionInline,]

admin.site.register(models.Project, ProjectAdmin)

admin.site.register(models.SingleBannerImage)
admin.site.register(models.SingleBannerVideo)
admin.site.register(models.ServiceCard)
admin.site.register(models.ProjectsPage)
admin.site.register(models.MainBanner)
