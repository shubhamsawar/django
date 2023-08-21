from django.contrib import admin
from . models import news
# Register your models here.
class news_admin(admin.ModelAdmin):
    list_display=['author','title','desc','date','urls']




admin.site.register(news,news_admin)
