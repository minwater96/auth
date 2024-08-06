from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username',)


class CustomAuthenticationForm(AuthenticationForm):
    pass