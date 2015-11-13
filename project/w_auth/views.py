from django.shortcuts import render
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from .forms import LoginForm

_login_form_template = "w_auth/test_auth_form.html"
# _success_url = reverse("main:profile")
_success_url = "profile"


def login(request):

    if not request.POST:
        form = LoginForm()
        t_context = {'login_form': form}
        return render(request, _login_form_template, t_context)
    else:
        t_context = {}
        form = LoginForm(request.POST)
        t_context['login_form'] = form
        if form.errors:
            t_context['errors'] = form.errors
            return render(request, _login_form_template, t_context)
        else:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # success_url = form.cleaned_data['next']

            user = auth.authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect(_success_url)
                else:
                    t_context['errors'] = ["Ваш аккаунт заблокирован"]
            else:
                t_context['errors'] = ["Неверный логин или пароль"]

            return render(request, _login_form_template, t_context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:home'))

