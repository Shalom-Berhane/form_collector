from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, edit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from cloudinary import CloudinaryImage
from PIL import Image

from .models import LostMemberModel, MemberFormModel
from django.shortcuts import render, get_object_or_404
from . import forms

from django.http import HttpResponse
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from urllib import request
from site_.settings import BASE_DIR
import io
import os


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


# To see all lost members in detail
class DetailLostMember(LoginRequiredMixin, DetailView):
    model = LostMemberModel


# To see detail registered member
class DetailMember(LoginRequiredMixin, DetailView):
    model = MemberFormModel


def member_context_data(pk, model):
    member = get_object_or_404(model, pk=pk)
    image_name = os.path.join(BASE_DIR, 'saved/' + str(member.user_name) + '_member.png')
    save_name = os.path.join(BASE_DIR, 'saved/saved_member.png')

    # response = requests.get(member.photo.url)
    # image_bytes = io.BytesIO(response.content)

    request.urlretrieve(member.photo.url, image_name)

    img = Image.open(image_name)
    resized_img = img.resize((200, 250))
    resized_img.save(save_name)

    doc = DocxTemplate(os.path.join(BASE_DIR, "members/templates/members/template.docx"))
    myimage = InlineImage(doc, image_descriptor=save_name, width=Mm(40), height=Mm(60))

    context = {'name': member.full_name, 'user_name': member.user_name, 'phone': member.phone_number,
               'image': myimage, 'address': member.address, 'current_member': member.current_member,
               'church_course': member.church_course, 'academic_department': member.academic_department,
               'additional_course': member.additional_course, 'academic_year': member.academic_year,
               'other_academic_year': member.other_academic_year, 'guardian_name': member.guardian_name,
               'guardian_number': member.guardian_number}
    doc.render(context)

    doc_io = io.BytesIO()  # create a file-like object
    doc.save(doc_io)  # save data to file-like object
    doc_io.seek(0)  # go to the beginning of the file-like object

    if os.path.exists(image_name):
        os.remove(image_name)
    if os.path.exists(save_name):
        os.remove(save_name)

    return doc_io.read()


def lost_context_data(pk, model):
    member = get_object_or_404(model, pk=pk)
    image_name = os.path.join(BASE_DIR, 'saved/' + str(member.author) + '_lost_member.png')
    save_name = os.path.join(BASE_DIR, 'saved/saved_lost_member.png')

    doc = DocxTemplate(os.path.join(BASE_DIR, "members/templates/members/lost_member_template.docx"))

    if member.photo:
        request.urlretrieve(member.photo.url, image_name)

        img = Image.open(image_name)
        resized_img = img.resize((200, 250))
        resized_img.save(save_name)
        myimage = InlineImage(doc, image_descriptor=save_name, width=Mm(40), height=Mm(60))
    else:
        myimage = "No photo provided."

    context = {'name': member.full_name, 'author': member.author, 'phone': member.phone_number,
               'image': myimage, 'address': member.address, 'participation': member.participation,
               'additional_reason': member.additional_reason, 'member1_name': member.member1_name,
               'member1_phone': member.member1_phone, 'member2_name': member.member2_name,
               'member2_phone': member.member2_phone, 'additional_advice': member.additional_advice}

    doc.render(context)

    doc_io = io.BytesIO()  # create a file-like object
    doc.save(doc_io)  # save data to file-like object
    doc_io.seek(0)  # go to the beginning of the file-like object

    if os.path.exists(image_name):
        os.remove(image_name)
    if os.path.exists(save_name):
        os.remove(save_name)

    return doc_io.read()


@staff_member_required
def render_docx_view(request, *args, **kwargs):
    pk = kwargs.get('pk')

    # call function
    doc_io_read = member_context_data(pk, MemberFormModel)

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(doc_io_read)
    response['Content-Disposition'] = "filename=generated_doc.docx"
    response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    return response


@staff_member_required
def render_lost_member_view(request, *args, **kwargs):
    pk = kwargs.get('pk')

    # call function
    doc_io_read = lost_context_data(pk, LostMemberModel)

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(doc_io_read)
    response['Content-Disposition'] = "filename=generated_doc.docx"
    response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    return response