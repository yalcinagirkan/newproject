from django.conf.urls import url

from blogsections.adminpanel.addtag.views import AddTagView

app_name= "addtag"
urlpatterns = [
    url(r'^addtag/$', AddTagView.as_view(), name="addtag"),
]
