from django.conf.urls import url, include
app_name = 'adminpanel'
urlpatterns = [
    url(r'^', include('blogsections.adminpanel.home.urls', namespace='home')),
    url(r'^', include('blogsections.adminpanel.taglist.urls', namespace='taglist')),
    url(r'^', include('blogsections.adminpanel.addtag.urls', namespace='addtag')),
    url(r'^', include('blogsections.adminpanel.user.urls', namespace='user')),

]

