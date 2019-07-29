from django.conf.urls import url

from blogsections.adminpanel.user.views import UserListView, UserDeleteView, UserCreateView, UserPasswordChangeView


app_name= "user"
urlpatterns = [
    url(r'^usercreate/$',UserCreateView.as_view(),name="usercreate"),
    url(r'^userlist/$', UserListView.as_view(), name="userlist"),
    url(r'^userlist/(?P<pk>\d+)/delete/', UserDeleteView.as_view(), name="userdelete"),
    url(r'^userlist/(?P<pk>\d+)/userupdate/', UserPasswordChangeView.as_view(), name="userupdate"),
    url(r'^(?P<pk>\d+)/adminupdate/', UserPasswordChangeView.as_view(), name="adminupdate"),

]
