from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('media/<str:filename>/', views.restricted_media, name="restricted_media"),
    path('media/<str:filename>/<int:download>/', views.restricted_media, name="restricted_media"),
]

urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
)

admin.site.site_header = _('Jack')
admin.site.site_title = _('Jack')
admin.site.index_title = ''
