from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
)
