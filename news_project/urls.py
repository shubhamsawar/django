
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include('news_app.urls',namespace= 'news_app')),
    path("", include('accounts.urls', namespace='accounts')),
    
]

urlpatterns+=static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)
