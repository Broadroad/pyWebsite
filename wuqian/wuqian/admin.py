from django.contrib import admin

# Register your models here.
from wuqian.models import about_wuqian
from wuqian.models import company_culture
from wuqian.models import contact_us
from wuqian.models import wuqian_business
from wuqian.models import home_page
from wuqian.models import social_ability
from wuqian.models import news
from wuqian.models import human_resources
from wuqian.models import upload_image

admin.site.register(home_page.HomePage)
admin.site.register(about_wuqian.AboutWuqian)
admin.site.register(company_culture.CompanyCulture)
admin.site.register(contact_us.ContactUs)
admin.site.register(social_ability.SocialAbility)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_type')
    search_fields = ('title',)
    list_filter = ('news_type',)

admin.site.register(news.News, NewsAdmin)
admin.site.register(wuqian_business.WuqianBusiness, NewsAdmin)
admin.site.register(human_resources.HumanResource)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', )
    search_field = ('image', )
admin.site.register(upload_image.UploadImage, ImageAdmin)
