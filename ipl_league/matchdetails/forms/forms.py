from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholders': 'Enter user Name'}),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholders': 'Enter password'}),
    )


class SignUpForm(forms.Form):
     username = forms.CharField(
         required=True,
         widget=forms.TextInput(
                 attrs={'class': 'input', 'type': 'text', 'placeholders': 'Enter user Name'}),
     )
     email = forms.EmailField(
         required=True,
         widget=forms.EmailInput(
             attrs={'class': 'input', 'type': 'mail', 'placeholders': 'Enter email'}),
     )
     password = forms.CharField(
         required=True,
         widget=forms.PasswordInput(
                 attrs={'class': 'input', 'type': 'password', 'placeholders': 'Enter password'}),
     )

