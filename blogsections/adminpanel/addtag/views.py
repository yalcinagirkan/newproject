
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AddTagView(LoginRequiredMixin,TemplateView):
    template_name = "addtag.html"
