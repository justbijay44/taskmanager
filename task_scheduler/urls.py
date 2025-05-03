from django.contrib import admin
from django.urls import path, include
from tasks.views import task_list

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    
    path('api/', include('tasks.api_urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('debug/', include('debug_toolbar.urls')),

    path('', task_list, name='task-list'),  # Root URL also points to home
]
