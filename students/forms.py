from django import forms
from django.contrib.auth.models import User

from .models import Student, Club, Group


class StudentForm(forms.ModelForm):
    new_group = forms.CharField(
        required=False,
        label='Новая группа',
        widget=forms.TextInput(attrs={'placeholder': 'Новая группа (если нет в списке)'}),
    )

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'group', 'new_group', 'clubs', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Возраст', 'min': 1}),
            'group': forms.Select(),
            'clubs': forms.CheckboxSelectMultiple(),
        }

    def save(self, commit=True):
        new_group_name = self.cleaned_data.get('new_group')
        if new_group_name:
            group, _ = Group.objects.get_or_create(name=new_group_name, defaults={'curator': 'Неизвестно'})
            self.instance.group = group
        return super().save(commit=commit)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают!')
        return cleaned_data