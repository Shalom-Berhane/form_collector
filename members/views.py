from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import LostMemberModel, MemberFormModel
from django.shortcuts import render
from . import forms
from .models import User

# User = get_user_model()


class Home(TemplateView):
    template_name = "home.html"


class SignUp(CreateView):

    form_class = forms.UserCreateForm

    success_url = reverse_lazy('members:login')
    template_name = "accounts/sign_up.html"


class MemberForm(CreateView, FormView):
    form_class = forms.MemberForm
    model = MemberFormModel

    success_url = reverse_lazy('members:home')
    template_name = "member_form.html"

    def form_valid(self, form):
        try:
            form.instance.user_name = self.request.user
            return super().form_valid(form)
        except:
            return render(self.request, "members/haveForm.html", self.get_context_data())


class LostMember(CreateView, FormView):
    form_class = forms.LostMemberCreateForm
    model = LostMemberModel

    success_url = reverse_lazy('members:home')
    template_name = "lost_member.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListMemberForm(ListView):

    model = MemberFormModel
    # template_name = "user_post_list.html"

    # def get_queryset(self):
    #     print(self.kwargs)
    #     user = get_object_or_404(User, username=self.kwargs.get('user_name'))
    #     return MemberFormModel.objects.filter(author=user)#.order_by('-date_posted')

    def get_context_data(self, *args, **kwargs):
        context = super(ListMemberForm, self).get_context_data(**kwargs)
        context['my_projects'] = MemberFormModel.objects.filter(user_name=self.request.user)
        return context


class ListLostMemberForm(ListView):

    model = LostMemberModel

    def get_context_data(self, *args, **kwargs):
        context = super(ListLostMemberForm, self).get_context_data(**kwargs)
        context['my_projects'] = LostMemberModel.objects.filter(author=self.request.user)
        return context


class DetailLostMember(DetailView):
    model = LostMemberModel
