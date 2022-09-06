from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView
from .models import LostMemberModel, MemberFormModel
from . import forms


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


class LostMember(CreateView, FormView):
    form_class = forms.LostMemberCreateForm
    model = LostMemberModel

    success_url = reverse_lazy('members:home')
    template_name = "lost_member.html"

