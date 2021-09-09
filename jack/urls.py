from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

from . import views

from two_factor.urls import urlpatterns as tf_urls
from two_factor.admin import AdminSiteOTPRequired

admin.site.__class__ = AdminSiteOTPRequired

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('media/<str:filename>/', views.restricted_media, name="restricted_media"),
    path('media/<str:filename>/<int:download>/', views.restricted_media, name="restricted_media"),
]

urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('', include('help.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include(tf_urls)),
)

admin.site.site_header = _('Jack Admin')
admin.site.site_title = ''
admin.site.index_title = ''
