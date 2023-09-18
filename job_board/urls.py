
from django.urls import path
from .views import job_board, job_detail

urlpatterns = [
    path("", job_board, name='job_board'),
    path("job/<int:pk>/", job_detail, name='job-detail'),
]
