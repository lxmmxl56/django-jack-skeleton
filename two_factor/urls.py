from django.urls import path

from two_factor.views import (
    BackupTokensView,
    DisableView,
    EmailDeleteView,
    EmailSetupView,
    ProfileView,
    QRGeneratorView,
    SetupCompleteView,
    SetupView,
)

core = [
    path(
        'account/security/two_factor/setup/',
        SetupView.as_view(),
        name='setup',
    ),
    path(
        'account/security/two_factor/qrcode/',
        QRGeneratorView.as_view(),
        name='qr',
    ),
    path(
        'account/security/two_factor/setup/complete/',
        SetupCompleteView.as_view(),
        name='setup_complete',
    ),
    path(
        'account/security/two_factor/backup/tokens/',
        BackupTokensView.as_view(),
        name='backup_tokens',
    ),
    path(
        'account/security/two_factor/backup/email/register/',
        EmailSetupView.as_view(),
        name='email_create',
    ),
    path(
        'account/security/two_factor/backup/email/unregister/<int:pk>/',
        EmailDeleteView.as_view(),
        name='email_delete',
    ),
]

profile = [
    path(
        'account/security/',
        ProfileView.as_view(),
        name='profile',
    ),
    path(
        'account/security/two_factor/disable/',
        DisableView.as_view(),
        name='disable',
    ),
]

urlpatterns = (core + profile, 'two_factor')
