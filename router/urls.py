from django.urls import path, include

app_name = 'router'

urlpatterns = [
    path('token/', include('jwt_authentication.urls'), name='jwt-authentication'),
    path('home/', include('home.urls'), name='home'),
    path('events/', include('events.urls'), name='events'),
    path('specials/', include('specials.urls'), name='specials'),
    path('about/', include('about.urls'), name='about'),
]
