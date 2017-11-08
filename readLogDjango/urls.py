from django.conf.urls import url
from django.contrib import admin
from viewlog import views
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^maillog/',views.readLog,name='readLog'),
    url(r'^login/$',views.login_view,name='login_view'),
    url(r'^logout/$',views.logout_view,name='logout_view'),
    url(r'^$',views.index,name='index')
]
