#change imports and models
#MUST ADD APPROPRIATE URLS/MODELS/VIEWS FOR THIS FILE

from django.forms import ModelForm
from aerinde.models import User


class UserForm(ModelForm):
    class Meta:
        model = User