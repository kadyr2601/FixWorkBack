from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

from restoration_page.models import Restoration

class Blog(models.Model):
    title_ru = models.CharField(max_length=512, verbose_name='Title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Title in English')
    first_paragraph_ru = models.TextField(verbose_name='First paragraph in Russian')
    first_paragraph_en = models.TextField(verbose_name='First paragraph in English')
    second_paragraph_ru = models.TextField(verbose_name='Second paragraph in Russian')
    second_paragraph_en = models.TextField(verbose_name='Second paragraph in English')
    third_paragraph_ru = models.TextField(verbose_name='Third paragraph in Russian')
    third_paragraph_en = models.TextField(verbose_name='Third paragraph in English')
    image = models.ImageField(upload_to='blog/', verbose_name='Image')
    slug = models.CharField(max_length=512, unique=True, verbose_name='Slug', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title_en)
            slug = original_slug
            counter = 1

            # Ensure initial instance has a unique slug
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            self.slug = slug

        portfolios = []
        for i in range(40):
            # Generate a unique slug for each portfolio instance
            unique_slug = f"{self.slug}-{i + 1}"
            while Blog.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{i + counter}"
                counter += 1

            new_portfolio = Blog(
                title_ru=self.title_ru,
                title_en=self.title_en,
                first_paragraph_ru=self.first_paragraph_ru,
                first_paragraph_en=self.first_paragraph_en,
                second_paragraph_ru=self.second_paragraph_ru,
                second_paragraph_en=self.second_paragraph_en,
                third_paragraph_ru=self.third_paragraph_ru,
                third_paragraph_en=self.third_paragraph_en,
                image=self.image,
                slug=unique_slug
            )
            portfolios.append(new_portfolio)

        # Bulk create the portfolio instances with unique slugs
        Blog.objects.bulk_create(portfolios)

        # Save the original instance
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         original_slug = slugify(self.title_en)
    #         slug = original_slug
    #         counter = 1
    #
    #         while Blog.objects.filter(slug=slug).exists():
    #             slug = f"{original_slug}-{counter}"
    #             counter += 1
    #         self.slug = slug
    #     portfolios = []
    #     for _ in range(40):
    #         new_portfolio = Blog(
    #             title_ru=self.title_ru, title_en=self.title_en,
    #             first_paragraph_ru=self.first_paragraph_ru, first_paragraph_en=self.first_paragraph_en,
    #             second_paragraph_ru=self.second_paragraph_ru, second_paragraph_en=self.second_paragraph_en,
    #             third_paragraph_ru=self.third_paragraph_ru, third_paragraph_en=self.third_paragraph_en,
    #             image=self.image, slug=self.slug
    #
    #         )
    #         portfolios.append(new_portfolio)
    #     Blog.objects.bulk_create(portfolios)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog List'

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
    slug = models.ForeignKey(Restoration, on_delete=models.CASCADE, to_field='slug', related_name="blogs_services", verbose_name='Select Restoration')

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Service Card Section'
        verbose_name_plural = 'Service Cards Sections'

class BlogsPage(models.Model):
    main_banner = models.OneToOneField(MainBanner, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Main Banner')
    single_banner_image = models.OneToOneField(SingleBannerImage, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Image Banner')
    services_banner = models.ManyToManyField(ServiceCard, blank=True, related_name='services_banner', verbose_name='Services Banner')
    single_banner_video = models.OneToOneField(SingleBannerVideo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Video Banner')

    class Meta:
        verbose_name = 'Blogs Page Widget'
        verbose_name_plural = 'Blogs Page Widgets'

    def clean(self):
        if BlogsPage.objects.exists() and not self.pk:
            raise ValidationError("Only one Blogs Page instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(BlogsPage, self).save(*args, **kwargs)

    def __str__(self):
        return "Blogs Page Instance"
