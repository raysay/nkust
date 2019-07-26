from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from allauth.socialaccount.forms import SignupForm
from allauth.socialaccount.models import SocialAccount
from urllib.request import urlopen
from django.conf import settings

from .import models

class PostForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = ('title', 'content','poster',)

User = get_user_model()


class MyCustomSocialSignupForm(SignupForm):
    # company_name = forms.CharField(label=_('公司名稱'))
    # cell_phone = forms.CharField(label=_('行動電話'))
    # office_phone = forms.CharField(label=_('辦公室電話'))
    # fax_number = forms.CharField(label=_('傳真機電話'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True
        # self.fields['company_name'].widget.attrs['placeholder'] = _('公司名稱')
    def save(self,request):
        user = super(MyCustomSocialSignupForm,self).save(request)
        user_data = SocialAccount.objects.filter(user=user)[0].extra_data
        # user_data = self.socialaccount_set.filter(provider='Google')[0].extra_data
        user.is_staff=False
        user.save()
        # user_profile = UserProfileInfo()
        # user_profile.user = user
        # user_profile.display_name =  user_data['name']
        # url = user_data['picture']
        # img_temp = NamedTemporaryFile()
        # img_temp.write(urlopen(url).read())
        # img_temp.flush()
        # user_profile.profile_pic.save(user_data['id'], File(img_temp))
        # user_profile.company_name = self.cleaned_data['company_name']
        # user_profile.cell_phone = self.cleaned_data['cell_phone']
        # user_profile.office_phone = self.cleaned_data['office_phone']
        # user_profile.fax_number = self.cleaned_data['fax_number']
        # user_profile.save()
        # send_mail("新使用者"+str(user_profile)+'已註冊', \
        #  '純文字提示訊息',\
        #  settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=True,\
        #  html_message="新使用者透過Google加入平台" )
        return user
