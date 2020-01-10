from django import forms
from .models import Freelancer

#DataFlair
class FreelancerCreate(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = '__all__'