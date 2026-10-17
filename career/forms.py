from django import forms

from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'mobile', 'resume']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': True,
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile Number',
                'required': True,
            }),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile'].strip()
        digits = mobile.replace('+', '').replace('-', '').replace(' ', '')
        if not digits.isdigit() or not (10 <= len(digits) <= 15):
            raise forms.ValidationError('Enter a valid mobile number (10 to 15 digits).')
        return mobile

    def clean_resume(self):
        resume = self.cleaned_data['resume']
        max_size = 5 * 1024 * 1024  # 5 MB
        if resume.size > max_size:
            raise forms.ValidationError('Resume file must be 5 MB or smaller.')
        return resume
