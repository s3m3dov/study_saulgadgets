from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Userprofile

class UserprofileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserprofileForm, self).__init__(*args, **kwargs)
        #TODO Learn this type of writing (above)
        # Adding 'input' class to form fields created by django (below)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input'

    class Meta:
        model = Userprofile
        fields = '__all__'
        exclude = ('user',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        #TODO Learn this type of writing (above)
        # Adding 'input' class to form fields created by django (below)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
