from django.contrib import admin
from .models import HomePage, AboutUs, Counter, SingleBannerImage, SingleBannerVideo, MainBanner, Partner, ServiceCard
from django import forms
from django.utils.safestring import mark_safe


admin.site.register(MainBanner)
admin.site.register(AboutUs)
admin.site.register(Counter)
admin.site.register(SingleBannerImage)
admin.site.register(Partner)
admin.site.register(SingleBannerVideo)
admin.site.register(ServiceCard)


class HomePageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HomePageForm, self).__init__(*args, **kwargs)

        self.fields['main_banner'].help_text = mark_safe(
            '<img src="/media/home_page_main_banner.png" width="450" style="margin-top:20px;">')
        self.fields['restoration_banner'].help_text = mark_safe(
            '<img src="/media/h_restoration_banner.png" width="450" style="margin-top:20px;">')
        self.fields['about_us'].help_text = mark_safe(
            '<img src="/media/h_about_us.png" width="450" style="margin-top:20px;">')
        self.fields['counter_banner'].help_text = mark_safe(
            '<img src="/media/h_counter.png" width="450" style="margin-top:20px;">')
        self.fields['single_banner_image'].help_text = mark_safe(
            '<img src="/media/h_s_image.png" width="450" style="margin-top:20px;">')
        self.fields['reviews_banner'].help_text = mark_safe(
            '<img src="/media/h_reviews.png" width="450" style="margin-top:20px;">')
        self.fields['services_banner'].help_text = mark_safe(
            '<img src="/media/h_services.png" width="450" style="margin-top:20px;">')
        self.fields['partners_banner'].help_text = mark_safe(
            '<img src="/media/h_partners.png" width="450" style="margin-top:20px;">')
        self.fields['single_banner_video'].help_text = mark_safe(
            '<img src="/media/hs-video.png" width="450" style="margin-top:20px;">')

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    form = HomePageForm