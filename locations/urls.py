from . import views
from django.urls import path


urlpatterns = [
    path('', views.LocationList.as_view(), name='home'),
    path('<slug:location_slug>/', views.LocationSingle.as_view(), name='location_single'),
    path('like/<slug:slug>', views.LocationLike.as_view(), name='location_like'),
]