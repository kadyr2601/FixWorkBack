from django.db import models

class Restoration(models.Model):
    Widths = (
        ('100', 'Full width'),
        ('40', 'Half width'),
    )
    banner_image = models.ImageField(upload_to='restoration/', verbose_name='Banner image', null=True, blank=True)
    desktop_height = models.PositiveIntegerField(default=869)
    mobile_height = models.PositiveIntegerField(default=348)
    desktop_width = models.CharField(max_length=3, choices=Widths, default='100')
    name_ru = models.CharField(max_length=512, verbose_name='Name in Russian')
    name_en = models.CharField(max_length=512, verbose_name='Name in English')
    slug = models.SlugField(max_length=512, unique=True)
    title_ru = models.CharField(max_length=512, verbose_name='Title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Title in English')
    description_ru = models.TextField(verbose_name='Description in Russian')
    description_en = models.TextField(verbose_name='Description in English')
    seo_title_ru = models.CharField(max_length=512, verbose_name='SEO Title in Russian')
    seo_title_en = models.CharField(max_length=512, verbose_name='SEO Title in English')
    seo_description_ru = models.TextField(verbose_name='SEO Description in Russian')
    seo_description_en = models.TextField(verbose_name='SEO Description in English')
    image_before = models.ImageField(upload_to='restoration/')
    image_after = models.ImageField(upload_to='restoration/')
    image_title_ru = models.CharField(max_length=512, verbose_name='Image title in Russian')
    image_title_en = models.CharField(max_length=512, verbose_name='Image title in English')
    services_background = models.ImageField(upload_to='restoration/', verbose_name='Services background image')
    faqs = models.ManyToManyField('FAQ', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.name_en.replace(' ', '-').lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Restoration'
        verbose_name_plural = 'Restoration List'

class RestorationService(models.Model):
    restoration = models.ForeignKey(Restoration, on_delete=models.CASCADE, related_name='services')
    title_ru = models.CharField(max_length=512, verbose_name='Service title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Service title in English')
    description_ru = models.TextField(verbose_name='Service description in Russian')
    description_en = models.TextField(verbose_name='Service description in English')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Restoration Service'
        verbose_name_plural = 'Restoration Services'

class FAQ(models.Model):
    question_ru = models.CharField(max_length=512, verbose_name='Question in Russian')
    question_en = models.CharField(max_length=512, verbose_name='Question in English')
    answer_ru = models.TextField(verbose_name='Answer in Russian')
    answer_en = models.TextField(verbose_name='Answer in English')

    def __str__(self):
        return self.question_en

    class Meta:
        verbose_name = 'Restoration FAQ'
        verbose_name_plural = 'Restoration FAQs'
