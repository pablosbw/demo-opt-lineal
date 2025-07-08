from django.urls import path
from .views import upload, results

urlpatterns = [
    path('', upload, name='home'),
    path('upload/', upload, name='upload'),
    path('results/', results, name='results'),
]
