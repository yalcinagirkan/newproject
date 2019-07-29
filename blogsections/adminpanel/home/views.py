from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView
# Create your views here.
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "taglist.html"
    login_url = '/login/'


class LoginView(BaseLoginView):
    form_class = AuthenticationForm
    template_name= 'login.html'


class LogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

