from django.conf.urls import url

from blogsections.adminpanel.taglist.views import TagListView

app_name= "taglist"
urlpatterns = [
    url(r'^taglist/$', TagListView.as_view(), name="taglist"),
]
