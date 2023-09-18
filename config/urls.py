"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import SignupView, CustomLogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('dash.urls'), name="dashboard"),
    path("job_board/", include('job_board.urls'), name='job_board'),
    path("trip/", include('trip.urls'), name='trip-home'),
    path("trip/accounts/", include('django.contrib.auth.urls')),
    path("trip/accounts/logout", CustomLogoutView.as_view(), name='logout'),
    path("trip/accounts/signup/", SignupView.as_view(), name="signup"),
    path("todo/", include("todo.urls"), name='register-todo'),
    path("links/", include("links.urls"), name='shortlink'),
    path('link_plant/', include('link_plant.urls'), name='link-list'),
]

'''
## package fully loaded (check DJ docs) ---> to see file path go to venv/django/contrib/auth...see how the library works
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']

'''

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
