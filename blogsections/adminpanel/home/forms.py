from django.forms import ModelForm

from blogsections.adminpanel.home.models import Home


class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = "__all__"
