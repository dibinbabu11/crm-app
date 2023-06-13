from django import forms
from . models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model: Record
        fields:['first_name','last_name','email','address','phone','city','state']