from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, edit
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import LostMemberModel, MemberFormModel
from django.shortcuts import render
from . import forms


class Home(LoginRequiredMixin, TemplateView):
    template_name = "home.html"


class SignUp(CreateView):

    form_class = forms.UserCreateForm

    success_url = reverse_lazy('members:login')
    template_name = "accounts/sign_up.html"


class MemberForm(LoginRequiredMixin, CreateView, edit.FormView):
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


class LostMember(LoginRequiredMixin, CreateView, edit.FormView):
    form_class = forms.LostMemberCreateForm
    model = LostMemberModel

    success_url = reverse_lazy('members:home')
    template_name = "lost_member.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListMemberForm(LoginRequiredMixin, ListView):

    model = MemberFormModel

    def get_context_data(self, *args, **kwargs):
        context = super(ListMemberForm, self).get_context_data(**kwargs)
        context['my_projects'] = MemberFormModel.objects.filter(user_name=self.request.user)
        return context


class ListLostMemberForm(LoginRequiredMixin, ListView):

    model = LostMemberModel

    def get_context_data(self, *args, **kwargs):
        context = super(ListLostMemberForm, self).get_context_data(**kwargs)
        context['my_projects'] = LostMemberModel.objects.filter(author=self.request.user)
        return context


class AllMembers(LoginRequiredMixin, ListView):

    model = MemberFormModel

    def get_context_data(self, *args, **kwargs):
        context = super(AllMembers, self).get_context_data(**kwargs)
        context['my_projects'] = MemberFormModel.objects.all()
        return context


class AllLostMember(LoginRequiredMixin, ListView):

    model = LostMemberModel

    def get_context_data(self, *args, **kwargs):
        context = super(AllLostMember, self).get_context_data(**kwargs)
        context['my_projects'] = LostMemberModel.objects.all()
        return context


class DetailLostMember(LoginRequiredMixin, DetailView):
    model = LostMemberModel


class DetailMember(LoginRequiredMixin, DetailView):
    model = MemberFormModel
