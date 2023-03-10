from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from auth_user.api import views
# from .views import MyTokenObtainPairView


urlpatterns = [

    url(r'^token/$', jwt_views.token_obtain_pair, name='token_obtain_pair'),
    url(r'^token/refresh/$', jwt_views.token_refresh, name='token_refresh'),

    url(r'^token/sliding/$', jwt_views.token_obtain_sliding,
        name='token_obtain_sliding'),
    url(r'^token/sliding/refresh/$', jwt_views.token_refresh_sliding,
        name='token_refresh_sliding'),

    url(r'^token/verify/$', jwt_views.token_verify, name='token_verify'),

    url(r'^register/$', views.vRegister),
    url('^login/$', views.vLogin, ),
    url('^logout/$', views.vLogout, ),

    url(r'^profile/$', views.vUserProfile),

    url(r'^deposite/$', views.vUserProfile_deposite, name="update_deposite"),
    url(r'^reset/$', views.vUserProfile_reset),

]
