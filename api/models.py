from django.core.exceptions import ValidationError
from django.db import models

class MainBanner(models.Model):
    Pages = (
        ('home', 'Home'),
        ('projects', 'Projects'),
        ('portfolio', 'Portfolio'),
        ('reviews', 'Reviews'),
        ('blog', 'Blog'),
        ('contact', 'Contact'),
    )
    Widths = (
        ('100', 'Full width'),
        ('40', 'Half width'),
    )
    page = models.CharField(max_length=20, choices=Pages, default='home', unique=True)
    image = models.ImageField(upload_to='banner/')
    desktop_height = models.PositiveIntegerField(default=386)
    desktop_width = models.CharField(max_length=3, choices=Widths, default='100')
    mobile_height = models.PositiveIntegerField(default=250)

    def __str__(self):
        return self.page

    class Meta:
        verbose_name = 'Main Banner'
        verbose_name_plural = 'Main Banners'


class Project(models.Model):
    title_ru = models.CharField(max_length=512, verbose_name='Project title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Project title in English')
    description_ru = models.TextField(verbose_name='Project description in Russian')
    description_en = models.TextField(verbose_name='Project description in English')
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ProjectSection(models.Model):
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sections')
    title_ru = models.CharField(max_length=512, verbose_name='Section title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Section title in English')
    description_ru = models.TextField(verbose_name='Section description in Russian')
    description_en = models.TextField(verbose_name='Section description in English')

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Project Section'
        verbose_name_plural = 'Project Sections'


class Portfolio(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        portfolios = []
        for _ in range(10):
            new_portfolio = Portfolio(title=self.title, image=self.image)
            portfolios.append(new_portfolio)
        Portfolio.objects.bulk_create(portfolios)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


class ServiceCard(models.Model):
    name_ru = models.CharField(max_length=256, verbose_name='Name in Russian')
    name_en = models.CharField(max_length=256, verbose_name='Name in English')
    icon = models.ImageField(upload_to='service-card/')

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = 'Service Card'
        verbose_name_plural = 'Service Cards'


class Service(models.Model):
    Pages = (
        ('home', 'Home'),
        ('projects', 'Projects'),
        ('portfolio', 'Portfolio'),
        ('reviews', 'Reviews'),
        ('blog', 'Blog'),
    )
    page = models.CharField(max_length=20, choices=Pages, default='home', unique=True)
    cards = models.ManyToManyField(ServiceCard)

    def __str__(self):
        return self.page

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class PageBanner(models.Model):
    Pages = (
        ('home', 'Home'),
        ('projects', 'Projects'),
        ('portfolio', 'Portfolio'),
        ('reviews', 'Reviews'),
        ('blog', 'Blog'),
    )
    Types = (
        ('video', 'Video'),
        ('image', 'Image'),
    )
    page = models.CharField(max_length=20, choices=Pages, default='home')
    type = models.CharField(max_length=20, choices=Types, default='image')
    title_ru = models.CharField(max_length=512, verbose_name='Title in Russian', null=True, blank=True)
    title_en = models.CharField(max_length=512, verbose_name='Title in English', null=True, blank=True)
    file = models.FileField(upload_to='banner/')
    button = models.BooleanField(default=False, verbose_name='Show button - "Leave an application"')
    desktop_height = models.PositiveIntegerField(default=500, verbose_name='Banner height on desktop in (px)')
    mobile_height = models.PositiveIntegerField(default=300, verbose_name='Banner height on mobile in (px)')

    def __str__(self):
        return f"{self.page} - {self.type}"

    def clean(self):
        super().clean()
        if PageBanner.objects.filter(page=self.page, type=self.type).exclude(id=self.id).exists():
            raise ValidationError(f"Баннер для страницы '{self.page}' и типа '{self.type}' уже существует.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Page Banner'
        verbose_name_plural = 'Page Banners'
        unique_together = ('page', 'type')


class Review(models.Model):
    fullname = models.CharField(max_length=128)
    location = models.CharField(max_length=256)
    comment_ru = models.TextField()
    comment_en = models.TextField()
    image = models.ImageField(upload_to='reviews/')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Blog(models.Model):
    title_ru = models.CharField(max_length=512, verbose_name='Title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Title in English')
    first_paragraph_ru = models.TextField(verbose_name='First paragraph in Russian')
    first_paragraph_en = models.TextField(verbose_name='First paragraph in English')
    second_paragraph_ru = models.TextField(verbose_name='Second paragraph in Russian')
    second_paragraph_en = models.TextField(verbose_name='Second paragraph in English')
    third_paragraph_ru = models.TextField(verbose_name='Third paragraph in Russian')
    third_paragraph_en = models.TextField(verbose_name='Third paragraph in English')
    image = models.ImageField(upload_to='blog/')
    slug = models.CharField(max_length=512, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = self.title_en.replace(' ', '-').lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Partner(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to='partners/')

    def save(self, *args, **kwargs):
        if not self.name:
            base_name = "Partner icon"  # Replace
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
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'


class Feedback(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

class FeedbackFile(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='feedbacks/')

    def __str__(self):
        return self.feedback.name

    class Meta:
        verbose_name = 'Feedback File'
        verbose_name_plural = 'Feedback Files'


class SEO(models.Model):
    Pages = (
        ('home', 'Home'),
        ('projects', 'Projects'),
        ('portfolio', 'Portfolio'),
        ('reviews', 'Reviews'),
        ('blog', 'Blog'),
        ('contact', 'Contact'),
    )
    page = models.CharField(max_length=20, choices=Pages, default='home', unique=True)
    title_ru = models.CharField(max_length=512, verbose_name='Title in Russian')
    title_en = models.CharField(max_length=512, verbose_name='Title in English')
    description_ru = models.TextField(verbose_name='Description in Russian')
    description_en = models.TextField(verbose_name='Description in English')

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO'


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
        verbose_name_plural = 'Restorations'


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