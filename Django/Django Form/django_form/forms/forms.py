from django import forms
from django.core import validators


class DjangoFrom(forms.Form):
    email = forms.EmailField(label="Enter you Email")
    password = forms.CharField( label="Enter Password", widget=forms.PasswordInput)

    CHOICES = [('male', 'male'), ('female', 'female')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    COLOR = [("red", "Red"), ("green", "Green"), ("yellow", "Yellow")]
    color = forms.MultipleChoiceField(choices=COLOR, widget=forms.CheckboxSelectMultiple)

class UploadFile(forms.Form):
    file = forms.FileField(validators=[validators.FileExtensionValidator(['png', 'jpeg'], "File format must be png/jpeg format")])

class Attr_Widget(forms.Form):
    name = forms.CharField(help_text="Enter your name", initial="Riyad")
    age = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Enter your age", 'class': "border-primary"}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))

class Form_Validation(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age = forms.IntegerField()

    # built-in validators
    address = forms.CharField(validators=[validators.MinLengthValidator(10, "Address must at least 10 chars")])

    def clean_name(self):
        val_name = self.cleaned_data['name']
        if len(val_name) < 10:
            raise forms.ValidationError("Name chars must be more than 10")
        return val_name
    
    # To validate multiple fields together or apply more complex rules
    def clean(self):
        cleaned_data = super().clean()
        val_email = cleaned_data.get('email')
        val_age = int(cleaned_data.get('age'))

        if '.com' not in val_email:
            raise forms.ValidationError("Email must contain '.com'")
        if val_age < 10 or val_age > 50:
            raise forms.ValidationError("Age must be in range 10 - 50")

        return cleaned_data