from django.urls import path
#
from .views import ContactView

app_name = 'contact_app'

urlpatterns = [
    path(
        'contact/',
        ContactView.as_view(),
        name='contact'
    )
]