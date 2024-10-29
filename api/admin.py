from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

admin.site.site_header = _("FixWorks")
admin.site.site_title = _("Панель администратора FixWorks")
admin.site.index_title = _("Добро пожаловать в админку FixWorks")

admin.site.register(models.MainBanner)

class ProjectSectionInline(admin.StackedInline):
    model = models.ProjectSection
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectSectionInline,]

admin.site.register(models.Project, ProjectAdmin)

admin.site.register(models.Portfolio)

admin.site.register(models.ServiceCard)

admin.site.register(models.Service)

admin.site.register(models.PageBanner)

admin.site.register(models.Review)

admin.site.register(models.Blog)


@admin.register(models.Partner)
class PartnerAdmin(admin.ModelAdmin):
    readonly_fields = ('name',)


class FeedbackFileInline(admin.StackedInline):
    model = models.FeedbackFile
    extra = 1
    readonly_fields = ('file_preview',)
    fields = ('file', 'file_preview',)

    def file_preview(self, obj):
        if obj.file:
            file_url = obj.file.url
            file_name = obj.file.name.lower()

            # Define allowed image and video extensions
            image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
            video_extensions = ('.mp4', '.webm', '.ogg')

            if file_name.endswith(image_extensions):
                # Display image preview
                return format_html(
                    '<img src="{}" width="500px" height="500px" style="object-fit: contain;" />',
                    file_url
                )
            elif file_name.endswith(video_extensions):
                # Display video preview
                return format_html(
                    '''
                    <video width="500px" height="500px" controls>
                        <source src="{}" type="video/{}">
                        Your browser does not support the video tag.
                    </video>
                    ''',
                    file_url,
                    file_name.split('.')[-1]  # Get the video file extension
                )
            else:
                # For other file types, provide a download link
                return format_html('<a href="{}">Download File</a>', file_url)
        return "No file uploaded"

    file_preview.short_description = 'File Preview'

@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    inlines = [FeedbackFileInline]


admin.site.register(models.SEO)
admin.site.register(models.FAQ)

class RestorationServiceInline(admin.StackedInline):
    model = models.RestorationService
    extra = 1


@admin.register(models.Restoration)
class RestorationAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    inlines = [RestorationServiceInline,]


