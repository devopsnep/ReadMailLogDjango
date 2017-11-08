
from django.conf.urls import url
from django.contrib import admin
from viewlog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^maillog/',views.readLog,name='readLog'),
    url(r'^$',views.index,name='index'),
]
