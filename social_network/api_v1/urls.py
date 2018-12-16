from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # apps
    path('', include('apps.user.urls')),
    path('', include('apps.post.urls')),

    # JWT auth
    path('token/auth/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),
]
