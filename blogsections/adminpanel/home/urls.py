from django.conf.urls import url

from blogsections.adminpanel.home.views import HomeView, LoginView, LogoutView

app_name = 'home'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='anasayfa'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
