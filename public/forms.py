from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["full_name","phone_number","email","country","password1","password2"]