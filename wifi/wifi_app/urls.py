from . import views
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
   
    path('',views.Detector,name='Detector'),
    path('getsettings',views.getsettings,name='getsettings'),
    path('getinterface',views.getinterface,name='getinterface'),
    path('enablemon',views.enablemon,name='enablemon'),
    path('settings',views.settings,name='settings'),
    path('saveDatabase',views.saveDatabase,name='saveDatabase'),
    path('resetDatabase',views.resetDatabase,name='resetDatabase'),
    path('diseablemon',views.diseablemon,name='diseablemon'),
    path('saveDetector',views.saveDetector,name='saveDetector'),
    path('start_deauth_detector',views.start_deauth_detector,name='start_deauth_detector'),
    path('stop_deauth_detector',views.stop_deauth_detector,name='stop_deauth_detector'),
    path('getdetector',views.getdetector,name='getdetector'),
     path('getsensorbutton',views.getsensorbutton,name='getsensorbutton'),
    
]
