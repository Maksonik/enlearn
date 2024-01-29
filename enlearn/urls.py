from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from word import views

router = DefaultRouter()
router.register(r'words', views.WordViewSet)
router.register(r'examples', views.ExampleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('account.urls')),
    path('words/', include('word.urls', namespace='words')),
    path('learning/', include('learning.urls', namespace='learning')),
    path('achieve/', include('achieve.urls', namespace='achieve')),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
