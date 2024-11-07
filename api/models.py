from django.db import models

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
        verbose_name_plural = 'Customer Feedbacks'

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
    title_ru = models.CharField(max_length=512, verbose_name='Title in Russian', default='Fixworks - реставрация и ремонт')
    title_en = models.CharField(max_length=512, verbose_name='Title in English', default='Fixworks - restoration and repair')
    description_ru = models.TextField(verbose_name='Description in Russian', default='Реставрация и ремонт мебели, дверей, окон, стен, полов, потолков и других поверхностей в Москве и Московской области.')
    description_en = models.TextField(verbose_name='Description in English', default='Furniture, doors, windows, walls, floors, ceilings and other surfaces restoration and repair in Moscow and Moscow region.')

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'SEO Settings for Pages'

    def __str__(self):
        return self.page
