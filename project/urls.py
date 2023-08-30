from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('post.urls', namespace='blog'))
]


urlpatterns += static(settings.STATIC_URL, documnent_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, documnent_root=settings.MEDIA_ROOT)