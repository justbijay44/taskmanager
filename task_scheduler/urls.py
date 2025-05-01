from django.contrib import admin
from django.urls import path, include
from users.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('users.urls')),
    path('tasks/', include('tasks.urls')),

    # path('home/', home, name='home'),
    path('', home, name='home'),  # Root URL also points to home
]
