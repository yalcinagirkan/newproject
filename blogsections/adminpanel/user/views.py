from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView, DeleteView, UpdateView

from blogsections.adminpanel.user.forms import UserPasswordChangeForm, UserCreateForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "userlist.html"
    context_object_name = "userlist"

    def get_queryset(self):
        return User.objects.all().exclude(is_superuser=True)


class UserCreateView(LoginRequiredMixin, FormView):
    template_name = 'usercreate.html'
    success_url = '/userlist'
    form_class = UserCreateForm

    def form_valid(self, form):
        form.save()
        return redirect('../userlist')

    def register(request):

        if request.method == 'POST':
            form = UserCreationForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect('./userlist')

            else:
                return render(request, './userlist', {'form': form})
        else:
            form = UserCreationForm()
            return render(request, './userlist', {'form': form})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User

    def get(self, request, *args, **kwargs):
        User.objects.get(id=self.kwargs.get('pk')).delete()
        return redirect('blogsections:user:userlist')


class UserPasswordChangeView(UpdateView):
    model = User
    template_name = "changepassword.html"
    form_class = UserPasswordChangeForm

    def get_success_url(self):
        return reverse('blogsections:user:userlist')

    def get_form_kwargs(self):
        user = User.objects.get(id=self.kwargs.get('pk'))

        if self.request.method == 'GET':
            kwargs = {}
            kwargs['user'] = user
            return kwargs
        kwargs = super(UserPasswordChangeView, self).get_form_kwargs()
        kwargs.pop('instance')
        kwargs['user'] = user
        return kwargs

