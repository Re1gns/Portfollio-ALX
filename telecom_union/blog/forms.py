from django import forms
from django.core.validators import EmailValidator
from .models import Comment


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(validators=[EmailValidator()], widget=forms.EmailInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class JoinForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='Age', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = forms.ChoiceField(label='Gender Identity', choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    
    address = forms.CharField(label='Address', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal_code = forms.CharField(label='Postal Code', max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    phone_number = forms.CharField(label='Phone Number', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    EMPLOYMENT_CHOICES = [
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
        ('student', 'Student'),
        ('other', 'Other'),
    ]
    employment_status = forms.ChoiceField(label='Employment Status', choices=EMPLOYMENT_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    
    job_title = forms.CharField(label='Job Title', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    HOW_HEARD_CHOICES = [
        ('social_media', 'Social Media'),
        ('friend', 'Friend'),
        ('website', 'Website'),
        ('other', 'Other'),
    ]
    how_heard = forms.ChoiceField(label='How Did You Hear About Us?', choices=HOW_HEARD_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    why_join = forms.CharField(label='Why do you want to join the union?', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    agree_to_terms = forms.BooleanField(
        label='I agree to the terms of service.',
        required=True,
    )