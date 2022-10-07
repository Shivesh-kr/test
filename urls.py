from . import views
from django.urls import path, include
from rest_framework import routers
from rest_auth.views import PasswordResetConfirmView


router = routers.DefaultRouter()
router.register('crimes', views.CrimeViewSet)
router.register('stations', views.StationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('rest/auth/', include('rest_auth.urls')),
    path('rest/auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    path('rest/auth/register/', include('rest_auth.registration.urls')),
] 