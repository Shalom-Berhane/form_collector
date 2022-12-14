from django import forms
from .models import LostMemberModel, MemberFormModel
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField

CHOICES = (
    ("1", "ኣብ ፍሉይ መደብ ጥራይ ይሳተፍ/ትሳተፍ"),
    ("2", "ኣብ ናይ ጽዋአ ኣኼባ ሳሕቲ ይሳተፍ/ትሳተፍ"),
    ("3", "ኣብ ኩሉ ዓይነት ኣገልግሎት ኣይሳተፍን/ኣይትሳተፍን"),
)


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ሙሉእ መጸዉዒ ስም ወይ ቁ.ስልኪ', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ምስጢራዊ መእተዊ (password)',
            'id': 'hi',
        }
))


class UserCreateForm(UserCreationForm):
    class Meta:

        fields = ('username', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'ሙሉእ መጸዉዒ ስም ወይ ቁ.ስልኪ'
        self.fields['password1'].label = 'ምስጢራዊ መእተዊ (password)'
        self.fields['password2'].label = 'እቲ ምስጢራዊ መእተዊ ድገሞ (Password confirmation)'
        self.fields['username'].help_text = """<ul>
        <li>ንኣብነት ኣቤል ክብሮም --> <b>(ኣቤል_ክብሮም፣ ኣቤል22፣ abelkb)</b></li>
        <li>ወይ ቁ.ስልኪ</li>
        <li>ክፍተት (space) ኣይፍቀድን’ዩ</li>
        <li>ምጸውዒ ስም እንተ ተታሒዙ ቁጽሪ እንዳ ወሰኽካ ክትምዝገብ ትኽእል አካ</li>
        </ul>
        """
        self.fields['password1'].help_text = """<ul>

        <li>ዝወሓደ 8 ፊደል ክኸውን ኣለዎ</li>
        <li>ኩሉ ቁጽሪ ክኸውን የብሉን</li>
        <li>ቀልጢፉ ዝግመት  ክኸውን የብሉን</li>
        </ul>
          """
        self.fields['password2'].help_text = """<ul>

        <li>እቲ ኣብ ላዕሊ ዝእተካዮ ምስጢራዊ መእተዊ ድገሞ</li>
        </ul>
          """


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
        self.fields['other_academic_year'].label = 'ደረጃ ትምህርቲ ካብ ኣብ ላዕሊ ተጠቂሱ ዘሎ ንላዕሊ ወይ ንታሕቲ እንተኾይኑ'
        self.fields['guardian_name'].label = 'ናይ ቀረባ ዋሕስ ምሉእ ስም'
        self.fields['guardian_number'].label = 'ቁ. ስልኪ ናይ ዋሕስካ/ኪ'


class LostMemberCreateForm(forms.ModelForm):
    class Meta:
        model = LostMemberModel
        fields = "__all__"
        exclude = ['author']
        widgets = {
            'member1_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'ምሉአ ስም',
                }),
            'member2_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'ምሉአ ስም',
            }),
            'member1_phone': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'ስልኪ ቅጽሩ/ራ'
                }),
            'member2_phone': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'ስልኪ ቅጽሩ/ራ'
            }),
            'additional_advice': forms.Textarea(attrs={
                'class': "form-control",
                'placeholder': 'ኣብ ምምላስ ኣባላት ክተኣታቶ ኣልዎ ትብልዎ ሓሳባት'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].label = 'ምሉአ ስም ናይ ኣብ ማሕበር ዘይነጥፍ/ዘይትነጥፍ ዘሎ/ዘላ ኣባል ማሕበር፥'
        self.fields['photo'].label = 'ናይ ካብ ኣገልግሎት ማሕበር ርሒቁ ዘሎ ስእሊ የእቱ'
        self.fields['photo'].help_text = "ክግደፍ ይከኣል’ዩ"
        self.fields['address'].label = 'ገዛዉቱ/ታ፥'
        self.fields['phone_number'].label = 'ስልኪ ቅጽሩ/ራ፥'
        self.fields['participation'].label = 'ገምጋም ህልው ኣገልግሎት ዘይነጥፍ ዘሎ ኣባል ማሕበር፥'
        self.fields['additional_reason'].label = 'ኣብ ላዕሊ ካብ ዝትጠቕሱ ወጻኢ ተወሳኪ ሓሳብ፥'
        self.fields['member1_name'].label = 'ምሉአ ስም'
        self.fields['member1_phone'].label = 'ስልኪ ቅጽሩ/ራ'
        self.fields['member2_name'].label = 'ምሉአ ስም'
        self.fields['member2_phone'].label = 'ስልኪ ቅጽሩ/ራ'
        self.fields['additional_advice'].label = 'ኣብ ምምላስ ኣባላት ክተኣታቶ ኣልዎ ትብልዎ ሓሳባት፥'
