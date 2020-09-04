from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from bootstrap_modal_forms.forms import BSModalModelForm


class CustomUserUpdateForm(BSModalModelForm):
    class Meta:
        model = User
        fields = ['email']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
