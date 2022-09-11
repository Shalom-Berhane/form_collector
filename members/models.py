from django.contrib import auth
from django.db import models
from django.contrib.auth import get_user_model

CHOICES =(
    ("1", "ኣብ ፍሉይ መደብ ጥራይ ይሳተፍ/ትሳተፍ"),
    ("2", "ኣብ ናይ ጽዋአ ኣኼባ ሳሕቲ ይሳተፍ/ትሳተፍ"),
    ("3", "ኣብ ኩሉ ዓይነት ኣገልግሎት ኣይሳተፍን/ኣይትሳተፍን"),
)

academic = (
    ("1", "11"),
    ("2", "12+1"),
    ("3", "12+2"),
    ("4", "12+3"),
    ("5", "12+4"),
    ("6", "12+5"),
)
new_user = get_user_model()

# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)


class User(new_user):

    def __str__(self):
        return str(self.username)


class LostMemberModel(models.Model):
    author = models.ForeignKey(new_user, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(
        help_text="Enter 6 digit roll number"
    )
    participation = models.CharField(choices=CHOICES, max_length=200)
    additional_reason = models.TextField()
    member1_name = models.CharField(max_length=200)
    member1_phone = models.IntegerField()
    member2_name = models.CharField(max_length=200)
    member2_phone = models.IntegerField()
    additional_advice = models.TextField()

    def __str__(self):
        return str(self.full_name)


class MemberFormModel(models.Model):
    user_name = models.OneToOneField(new_user, related_name="posts", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media',  blank=True, null=True)
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    current_member = models.CharField(max_length=200)
    church_course = models.CharField(max_length=200)
    academic_department = models.CharField(max_length=200)
    additional_course = models.CharField(max_length=200)
    academic_year = models.CharField(choices=academic, max_length=200)
    other_academic_year = models.CharField(max_length=200)
    guardian_name = models.CharField(max_length=200)
    guardian_number = models.IntegerField()

    def __str__(self):
        return str(self.user_name)
