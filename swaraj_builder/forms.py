from swaraj_builder.models import Quest
from django import forms

class QuestForm(forms.Form):
    first_name = forms.CharField(label='Enter name',max_length=20)
    phone = forms.CharField(label='Enter Phone No.',max_length=20)
    subject = forms.CharField(label='Enter the subject',max_length=50)
    message = forms.TextInput()

