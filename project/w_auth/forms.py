from django import forms


class LoginForm(forms.Form):
    def __init__(self):
        super(LoginForm, self).__init__(
            auto_id='%s',
            label_suffix='',
        )

    email = forms.EmailField(label='email',
                             widget=forms.TextInput(
                                 attrs={'class': ''}
                             ))

    password = forms.CharField(label='password',
                               widget=forms.PasswordInput(
                                   attrs={'class': ''}
                               ))
