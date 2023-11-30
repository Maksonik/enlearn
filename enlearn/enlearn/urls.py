from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from word import views

router = DefaultRouter()
router.register(r'words', views.WordViewSet)

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('words/', include('word.urls')),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
