from django import forms
from login import models

# class SignUp_Placeholder:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         field_names = [field_name for field_name, _ in self.fields.items()]
#         for field_name in field_names:
#             field = self.fields.get(field_name)
#             field.widget.attrs.update({'placeholder': field.label})

# class Student_LoginForm(forms.Form):
#     Roll_Number = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'T21011'}) )
#     Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'XXXXXX'}))


class SignupForm(forms.ModelForm):
    class Meta:
        model = models.Signup_Form
        fields = '__all__'
