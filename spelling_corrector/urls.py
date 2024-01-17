from django.urls import path
from spelling_corrector.views import check_spelling


urlpatterns = [
    path('check_spelling/', check_spelling, name='check_spelling'),
]
