from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birthplace', 'residence', 'age', 'university', 'hobbies']  # specialty sahəsini çıxarın
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthplace': forms.TextInput(attrs={'class': 'form-control'}),
            'residence': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control'}),
        }
