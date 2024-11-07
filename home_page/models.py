from django.core.exceptions import ValidationError
from django.db import models
from restoration_page.models import Restoration
from reviews_page.models import Review


class AboutUs(models.Model):
    image = models.ImageField(upload_to='about_us_image', verbose_name='Image')
    header_text_ru = models.CharField(max_length=255, verbose_name='Header in Russian')
    header_text_en = models.CharField(max_length=255, verbose_name='Header in English')
    text_ru = models.TextField(verbose_name='Text in Russian')
    text_en = models.TextField(verbose_name='Text in English')

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Section'

    def clean(self):
        if AboutUs.objects.exists() and not self.pk:
            raise ValidationError("Only one About Us instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(AboutUs, self).save(*args, **kwargs)

    def __str__(self):
        return "About Us Section Instance"

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

class Counter(models.Model):
    number = models.IntegerField(verbose_name='Number')
    text_ru = models.CharField(max_length=255, verbose_name='Text in Russian')
    text_en = models.CharField(max_length=255, verbose_name='Text in English')

    class Meta:
        verbose_name = 'Counter Section'
        verbose_name_plural = 'Counter Sections'

    def __str__(self):
        return f"{self.number} - {self.text_en}"

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

class Partner(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True, verbose_name='Name of the Partner')
    image = models.ImageField(upload_to='partners/', verbose_name='Image')

    def save(self, *args, **kwargs):
        if not self.name:
            base_name = "Partner icon"
            counter = 1
            new_name = base_name
            while Partner.objects.filter(name=new_name).exists():
                new_name = f"{base_name} {counter}"
                counter += 1
            self.name = new_name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner Section'
        verbose_name_plural = 'Partners Sections'

class ServiceCard(models.Model):
    name_ru = models.CharField(max_length=256, verbose_name='Service Name in Russian')
    name_en = models.CharField(max_length=256, verbose_name='Service Name in English')
    icon = models.ImageField(upload_to='service-card/', verbose_name='Service Card Icon')
    slug = models.ForeignKey(Restoration, on_delete=models.CASCADE, to_field='slug', verbose_name='Select Restoration')

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Service Card Section'
        verbose_name_plural = 'Service Cards Sections'

class HomePage(models.Model):
    main_banner = models.OneToOneField(MainBanner, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Main Banner')
    restoration_banner = models.ManyToManyField(ServiceCard, blank=True, verbose_name='Restoration Banner')
    about_us = models.OneToOneField(AboutUs, on_delete=models.CASCADE, null=True, blank=True, verbose_name='About Us')
    counter_banner = models.ManyToManyField(Counter, blank=True, verbose_name='Counter Banner')
    single_banner_image = models.OneToOneField(SingleBannerImage, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Image Banner')
    reviews_banner = models.ManyToManyField(Review, blank=True, verbose_name='Reviews Banner')
    services_banner = models.ManyToManyField(ServiceCard, blank=True, related_name='services_banner', verbose_name='Services Banner')
    partners_banner = models.ManyToManyField(Partner, blank=True, verbose_name='Partners Banner')
    single_banner_video = models.OneToOneField(SingleBannerVideo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Video Banner')

    class Meta:
        verbose_name = 'Home Page Widget'
        verbose_name_plural = 'Home Page Widgets'

    def clean(self):
        if HomePage.objects.exists() and not self.pk:
            raise ValidationError("Only one HomePage instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(HomePage, self).save(*args, **kwargs)

    def __str__(self):
        return "Home Page Instance"




