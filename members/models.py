from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

CHOICES = (
    ("ኣብ ፍሉይ መደብ ጥራይ ይሳተፍ/ትሳተፍ", "ኣብ ፍሉይ መደብ ጥራይ ይሳተፍ/ትሳተፍ"),
    ("ኣብ ናይ ጽዋአ ኣኼባ ሳሕቲ ይሳተፍ/ትሳተፍ", "ኣብ ናይ ጽዋአ ኣኼባ ሳሕቲ ይሳተፍ/ትሳተፍ"),
    ("ኣብ ኩሉ ዓይነት ኣገልግሎት ኣይሳተፍን/ኣይትሳተፍን", "ኣብ ኩሉ ዓይነት ኣገልግሎት ኣይሳተፍን/ኣይትሳተፍን"),
)

membership = (
    ("ክፍሊ ምክትታል ኣባላት", "ክፍሊ ምክትታል ኣባላት"),
    ("ክፍሊ ልምዓት", "ክፍሊ ልምዓት"),
    ("ክፍሊ ትምህርቲ", "ክፍሊ ትምህርቲ"),
    ("ክፍሊ ስነጥበብ", "ክፍሊ ስነጥበብ"),
    ("ክፍሊ መዝሙር", "ክፍሊ መዝሙር"),
)

academic = (
    ("11", "11"),
    ("12", "12"),
    ("12+1", "12+1"),
    ("12+2", "12+2"),
    ("12+3", "12+3"),
    ("12+4", "12+4"),
    ("12+5", "12+5"),
)
new_user = get_user_model()


class User(new_user):

    def __str__(self):
        return str(self.username)


class LostMemberModel(models.Model):
    author = models.ForeignKey(new_user, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    photo = CloudinaryField('image', blank=True, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(
        # help_text="Enter 6 digit roll number"
    )
    participation = models.CharField(choices=CHOICES, max_length=200, blank=True)
    additional_reason = models.TextField(blank=True)
    member1_name = models.CharField(max_length=200)
    member1_phone = models.IntegerField()
    member2_name = models.CharField(max_length=200, blank=True, null=True)
    member2_phone = models.IntegerField(blank=True, null=True)
    additional_advice = models.TextField()

    def __str__(self):
        return str(self.full_name)


class MemberFormModel(models.Model):
    user_name = models.OneToOneField(new_user, related_name="posts", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    photo = CloudinaryField('image')
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    current_member = models.CharField(choices=membership, max_length=250)
    church_course = models.TextField()
    academic_department = models.TextField()
    additional_course = models.CharField(max_length=200)
    academic_year = models.CharField(choices=academic, max_length=200, blank=True)
    other_academic_year = models.CharField(max_length=200, blank=True)
    guardian_name = models.CharField(max_length=200)
    guardian_number = models.IntegerField()

    def __str__(self):
        return str(self.full_name)
