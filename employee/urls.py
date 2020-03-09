from .views import main,table_view
from django.urls import path


urlpatterns = [
    path('', main, name='main'),
    path('table/',table_view, name='table')
]

