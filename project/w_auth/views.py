from django.contrib import auth
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import JsonResponse, HttpResponseBadRequest

from .forms import LoginForm

def login(request):
    resp_data = {'success': False}

    if not request.POST:
        return HttpResponseBadRequest()
    else:
        form = LoginForm(request.POST)
        if form.errors:
            # resp_data['errors'] = '<br>'.join(['{}: {}'.format(k, v) for k, v in form.errors.items()])
            resp_data['errors'] = {f: e.get_json_data() for f, e in form.errors.items()}
            print(form.errors)
            print(form.errors.items())
        else:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    resp_data["success"] = True
                else:
                    resp_data['errors'] = "Ваш аккаунт заблокирован"
            else:
                resp_data['errors'] = "Неверный логин или пароль"

        return JsonResponse(resp_data)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))

