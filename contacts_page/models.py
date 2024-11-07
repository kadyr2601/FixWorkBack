from django.core.exceptions import ValidationError
from django.db import models

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

class Email(models.Model):
    email = models.EmailField(max_length=255, verbose_name='Email')
    description_ru = models.CharField(max_length=255, verbose_name='Description in Russian')
    description_en = models.CharField(max_length=255, verbose_name='Description in English')

    class Meta:
        verbose_name = 'Email Section'
        verbose_name_plural = 'Email Section'

    def __str__(self):
        return self.email

class Phone(models.Model):
    phone = models.CharField(max_length=255, verbose_name='Phone')
    description_ru = models.CharField(max_length=255, verbose_name='Description in Russian')
    description_en = models.CharField(max_length=255, verbose_name='Description in English')

    class Meta:
        verbose_name = 'Phone Section'
        verbose_name_plural = 'Phone Section'

    def __str__(self):
        return self.phone

class ContactsPage(models.Model):
    main_banner = models.OneToOneField(MainBanner, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Main Banner')
    single_banner_image = models.OneToOneField(SingleBannerImage, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Image Banner')
    emails = models.ManyToManyField(Email, verbose_name='Emails', blank=True)
    phones = models.ManyToManyField(Phone, verbose_name='Phones', blank=True)

    class Meta:
        verbose_name = 'Contacts Page Widget'
        verbose_name_plural = 'Contacts Page Widgets'

    def clean(self):
        if ContactsPage.objects.exists() and not self.pk:
            raise ValidationError("Only one Contacts Page instance is allowed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ContactsPage, self).save(*args, **kwargs)

    def __str__(self):
        return "Contacts Page Instance"
