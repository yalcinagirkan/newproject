from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from blogsections.adminpanel.taglist.models import Post


class TagListView(LoginRequiredMixin, TemplateView):
    template_name = 'taglist.html'
    model = Post
