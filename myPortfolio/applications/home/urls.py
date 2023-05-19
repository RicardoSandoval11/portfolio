from django.urls import path
#
from .views import HomeView, AboutView

app_name = 'home_app'

urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home'
    ),
    path(
        'about-me/',
        AboutView.as_view(),
        name='about'
    )
]
