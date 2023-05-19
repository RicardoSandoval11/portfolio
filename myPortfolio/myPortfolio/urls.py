
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-portfolio/', admin.site.urls),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.skills.urls')),
    re_path('', include('applications.projects.urls')),
    path('captcha/', include('captcha.urls')),
    re_path('', include('applications.msgs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

