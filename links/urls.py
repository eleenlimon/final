from django.urls import path # copy/paste from config folder urls.py
from .views import shortlink, root_link, add_link

urlpatterns = [
    path("", shortlink, name="shortlink"), #include this path on config . urls.py too
    path("<str:link_slug>/", root_link, name='root-link'),
    path("link/create", add_link, name="create-link"),
]
