from django import forms
from .models import Lead, Tutor

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'class_level', 'subjects', 'city', 'locality', 'mobile_no']

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['name', 'class_level', 'subjects', 'city', 'locality', 'mobile_no']
