#change imports and models
#MUST ADD APPROPRIATE URLS/MODELS/VIEWS FOR THIS FILE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from models import User, List, Task
# from django.contrib.auth.models import User not used because now we are using Player which is a custom model


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def clean_username(self):

        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ('name',)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('task', 'deadline','list')