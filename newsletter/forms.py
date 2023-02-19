from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import NewsletterSignup

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ('name', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Subscribe', css_class='btn-black rounded-0'))
