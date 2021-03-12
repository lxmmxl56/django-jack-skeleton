from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    def user_link(self, obj):
        if obj.user is not None:
            username = obj.user.username
            user_id = obj.user.id
            url = reverse('admin:auth_user_change', args=[user_id])
            link = '<a href="%s">%s</a>' % (url, username)
            return mark_safe(link)
        else:
            return None

    raw_id_fields = ('user',)
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
    )
    list_display = (
        'id',
        'user_link',
        'email_confirmed',
    )
    list_filter = ('email_confirmed',)


admin.site.register(Profile, ProfileAdmin)
