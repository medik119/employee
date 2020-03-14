from .views import main, table_view,SignLoginView,OutLogoutView,ChangeView
from django.urls import path


urlpatterns = [
    path('', main,name= 'main' ),
    path('table/change/<int:pk>/',ChangeView.as_view(),name='change'),
    path('table/',table_view, name='table'),
    path('account/login/',SignLoginView.as_view(),name = 'login'),
    path('account/logout/',OutLogoutView.as_view(),name = 'logout'),
]

