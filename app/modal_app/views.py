from django.urls import reverse_lazy
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalLoginView
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .forms import CustomUserUpdateForm, CustomAuthenticationForm
from django.contrib.auth.models import User


class index(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'modal/index.html', {'user': request.user, 'is_authenticated': 1})
        return render(request, 'modal/index.html', {'is_authenticated': 0})


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2']


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'modal/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('modal:index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'modal/login.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('index'))


class UpdateView(BSModalUpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'modal/update.html'
    success_message = 'Success: Your email has been updated.'
    success_url = reverse_lazy('modal:index')


class user(View):
    def get(self, request):
        data = dict()
        if request.user.is_authenticated:
            data['table'] = render_to_string(
                'modal/_user_card.html',
                {'user': request.user},
                request=request
            )
            return JsonResponse(data)