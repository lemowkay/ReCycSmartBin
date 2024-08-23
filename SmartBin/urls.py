from django.urls import path
from . import views

# Define URL patterns for the ReCycSmartBin app
urlpatterns = [
    path('', views.home, name='SmartBin-home'),
    path('about/',views.about, name='SmartBin-about'),
    path('posts/', views.posts, name='SmartBin-posts'),
    path('map/', views.map_view, name='map'),
    path('contact/', views.contact, name='SmartBin-contact'),
    path('services/', views.services, name='SmartBin-services'),
    path('userpage/', views.userpage, name='userpage'),
    path('recycling-tips/', views.recycleTip, name='recycling_tips'),
    path('rewards/', views.rewardpage, name='rewards'),
    path('upload_slip/', views.upload_slip, name='upload_slip'),
    path('logout/', views.logout_view, name='logout'),
    path('scan/', views.scan_view, name='scan'),
    path('price/', views.reward_price, name='price'),
    path('pickup/', views.pickup, name='pickup'),
    path('request/', views.pickup_request, name='request'),
    path('history/', views.pickup_history, name='history'),
    path('report/', views.pickup_Report, name='report'),
]