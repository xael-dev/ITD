from django import forms
from emailstore.models import Email

class EmailForm(forms.ModelForm):
    email = forms.CharField(required = False)

    class Meta:
        model = Email
        fields = ('email', ) #Comma added to create a tuple arrangement not inferred datatype