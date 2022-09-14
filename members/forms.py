from django import forms
from .models import LostMemberModel, MemberFormModel
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

CHOICES = (
    ("1", "ኣብ ፍሉይ መደብ ጥራይ ይሳተፍ/ትሳተፍ"),
    ("2", "ኣብ ናይ ጽዋአ ኣኼባ ሳሕቲ ይሳተፍ/ትሳተፍ"),
    ("3", "ኣብ ኩሉ ዓይነት ኣገልግሎት ኣይሳተፍን/ኣይትሳተፍን"),
)


class UserCreateForm(UserCreationForm):
    class Meta:

        fields = ('username', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'


class MemberForm(forms.ModelForm):
    class Meta:
        model = MemberFormModel
        fields = "__all__"
        # fields = ('full_name', 'phone_number')
        exclude = ['user_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'ምሉአ ስም'
        self.fields['photo'].label = 'ናትካ ስእሊ የእቱ'
        self.fields['phone_number'].label = 'ቁ. ስልኪ'
        self.fields['address'].label = 'ህልው ገዛወቲ'
        self.fields['current_member'].label = 'ህልው ክፍሊ'
        self.fields['church_course'].label = 'ቅድሚ ሕጂ ዝወሰድካዮ/ክዮ መንፈሳዊ ትምህርቲ(ኮርስ)'
        self.fields['academic_department'].label = 'ዓለማዊ ዝወዳእካዮ/ክዮ ዓወደ ትምህርቲ'
        self.fields['additional_course'].label = 'ምያ ወይ ስራሕ'
        self.fields['academic_year'].label = 'ደረጃ ትምህርቲ'
        self.fields['other_academic_year'].label = 'ካብ ኣብላዕሊ ተጠቂሱ ዘሎ ደረጃ ትምህርቲ ወጻኢ'
        self.fields['guardian_name'].label = 'ናይ ቀረባ ዋሕስ ምሉእ ስም'
        self.fields['guardian_number'].label = 'ቁ. ስልኪ ናይ ዋሕስካ/ኪ'


class LostMemberCreateForm(forms.ModelForm):
    class Meta:
        model = LostMemberModel
        fields = "__all__"
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'ምሉአ ስም ናይ ኣብ ማሕበር ዘይነጥፍ/ዘይትነጥፍ ዘሎ/ዘላ ኣባል ምሕበር፥'
        self.fields['photo'].label = 'ናይ ካብ ኣገልግሎት ማሕበር ርሒቁ ዘሎ ስእሊ የእቱ'
        self.fields['address'].label = 'ገዛዉቱ/ታ፥'
        self.fields['phone_number'].label = 'ስልኪ ቅጽሩ/ራ፥'
        self.fields['participation'].label = 'ገምጋም ህልው ኣገልግሎት ዘይነጥፍ ዘሎ ኣባል ማሕበር፥'
        self.fields['additional_reason'].label = 'ኣብ ላዕሊ ካብ ዝትጠቕሱ ወጻኢ ተወሳኪ ሓሳብ፥'
        self.fields['member1_name'].label = 'ምሉአ ስም ናይ ቀዳማይ ኣባል ማሕበር'
        self.fields['member1_phone'].label = 'ስልኪ ቅጽሩ/ራ ናይ ቀዳማይ ኣባል ማሕበር'
        self.fields['member2_name'].label = 'ምሉአ ስም ናይ ካላኣይ ኣባል ማሕበር'
        self.fields['member2_phone'].label = 'ስልኪ ቅጽሩ/ራ ናይ ካላኣይ ኣባል ማሕበር'
        self.fields['additional_advice'].label = 'ኣብ ምምላስ ኣባላት ክተኣታቶ ኣልዎ ትብልዎ ሓሳባት፥'
