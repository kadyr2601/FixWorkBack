from django.core.exceptions import ValidationError
from django.db import models
from restoration_page.models import Restoration


class Project(models.Model):
    title_ru = models.CharField(max_length=512, verbose_name='Project title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Project title in English')
    description_ru = models.TextField(verbose_name='Project description in Russian')
    description_en = models.TextField(verbose_name='Project description in English')
    image = models.ImageField(upload_to='projects/', verbose_name='Project Image')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project List'

class ProjectSection(models.Model):
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sections', verbose_name='Select Project')
    title_ru = models.CharField(max_length=512, verbose_name='Section title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Section title in English')
    description_ru = models.TextField(verbose_name='Section description in Russian')
    description_en = models.TextField(verbose_name='Section description in English')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Project Details'
        verbose_name_plural = 'Project Details'

class SingleBannerImage(models.Model):
    image = models.ImageField(upload_to='single_banner_image', verbose_name='Image')
    header_text_ru = models.CharField(max_length=255, verbose_name='Header in Russian')
    header_text_en = models.CharField(max_length=255, verbose_name='Header in English')

    class Meta:
        verbose_name = 'Image Banner Section'
        verbose_name_plural = 'Image Banner Section'

    def clean(self):
        if SingleBannerImage.objects.exists() and not self.pk:
            raise ValidationError("Only one Single Banner Image instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SingleBannerImage, self).save(*args, **kwargs)

    def __str__(self):
        return "Image Banner Instance"

class SingleBannerVideo(models.Model):
    video = models.FileField(upload_to='single_banner_video', verbose_name='Video')
    header_text_ru = models.CharField(max_length=255, verbose_name='Header in Russian')
    header_text_en = models.CharField(max_length=255, verbose_name='Header in English')

    class Meta:
        verbose_name = 'Video Banner Section'
        verbose_name_plural = 'Video Banner Section'

    def clean(self):
        if SingleBannerVideo.objects.exists() and not self.pk:
            raise ValidationError("Only one Single Banner Video instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SingleBannerVideo, self).save(*args, **kwargs)

    def __str__(self):
        return "Video Banner Instance"

class MainBanner(models.Model):
    Widths = (
        ('100', 'Full width'),
        ('40', 'Half width'),
    )
    image = models.ImageField(upload_to='banner/', verbose_name='Image')
    desktop_height = models.PositiveIntegerField(default=386, verbose_name='Desktop Height')
    desktop_width = models.CharField(max_length=3, choices=Widths, default='100', verbose_name='Desktop Width')
    mobile_height = models.PositiveIntegerField(default=250, verbose_name='Mobile Height')

    class Meta:
        verbose_name = 'Main Banner Section'
        verbose_name_plural = 'Main Banner Section'

    def clean(self):
        if MainBanner.objects.exists() and not self.pk:
            raise ValidationError("Only one Main Banner instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(MainBanner, self).save(*args, **kwargs)

    def __str__(self):
        return "Main Banner Instance"

class ServiceCard(models.Model):
    name_ru = models.CharField(max_length=256, verbose_name='Service Name in Russian')
    name_en = models.CharField(max_length=256, verbose_name='Service Name in English')
    icon = models.ImageField(upload_to='service-card/', verbose_name='Service Card Icon')
    slug = models.ForeignKey(Restoration, on_delete=models.CASCADE, to_field='slug', related_name="projects_services", verbose_name='Select Restoration')

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Service Card Section'
        verbose_name_plural = 'Service Cards Sections'

class ProjectsPage(models.Model):
    main_banner = models.OneToOneField(MainBanner, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Main Banner')
    single_banner_image = models.OneToOneField(SingleBannerImage, null=True, on_delete=models.CASCADE, blank=True, verbose_name='Image Banner')
    services_banner = models.ManyToManyField(ServiceCard, blank=True, related_name='services_banner', verbose_name='Services Banner')
    single_banner_video = models.OneToOneField(SingleBannerVideo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Video Banner')

    class Meta:
        verbose_name = 'Projects Page Widget'
        verbose_name_plural = 'Projects Page Widgets'

    def clean(self):
        if ProjectsPage.objects.exists() and not self.pk:
            raise ValidationError("Only one Projects instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ProjectsPage, self).save(*args, **kwargs)

    def __str__(self):
        return "Projects Page Instance"
