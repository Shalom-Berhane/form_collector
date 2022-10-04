from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .forms import UserLoginForm

app_name = 'members'

urlpatterns = [
    path("",
         views.Home.as_view(),
         name='home'),
    path("accounts/login/",
         auth_views.LoginView.as_view(
             template_name="accounts/login.html",
             authentication_form=UserLoginForm
         ),
         name='login'),
    path("logout/",
         auth_views.LogoutView.as_view(),
         name="logout"),
    path("signup/",
         views.SignUp.as_view(),
         name="signup"),
    path("form/",
         views.LostMember.as_view(),
         name="form"),
    path("member_form/",
         views.MemberForm.as_view(),
         name="member_form"),
    path("my_form/",
         views.ListMemberForm.as_view(),
         name="my_form"),
    path("lost_list/",
         views.ListLostMemberForm.as_view(),
         name="lost_member_list"),
    path("all_lost_list/",
         views.AllLostMember.as_view(),
         name="all_lost_members"),
    path("all_member_list/",
         views.AllMembers.as_view(),
         name="all_members"),
    path("detail/<pk>/",
         views.DetailLostMember.as_view(),
         name="detail"),
    path("detail_member/<pk>/",
         views.DetailMember.as_view(),
         name="detail_member"),
    path("save/<pk>/",
         views.render_docx_view,
         name='save'),
    path("save_lost_member/<pk>/",
         views.render_lost_member_view,
         name='save_lost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
