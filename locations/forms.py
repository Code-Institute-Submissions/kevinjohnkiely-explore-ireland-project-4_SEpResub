from .models import Comment, Location, Profile
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """
    This class sets up the Comment Form and allows some
    customizations of attributes
    """
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Your Comments..."


class LocationForm(forms.ModelForm):
    """
    This class sets up the Location Form and allows some
    customizations of attributes
    """
    class Meta:
        model = Location
        fields = ('title', 'region', 'body', 'location_image', 'status')
        widgets = {
            'body': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Location Description"
        self.fields[
            'location_image'
            ].label = "Please upload a photo of location here! (Optional)"
        self.fields['status'].label = "Publish or Save Draft"


class ProfileForm(forms.ModelForm):
    """
    This class sets up the User Profile Form and allows some
    customizations of attributes
    """
    class Meta:
        model = Profile
        fields = ('full_name', 'location', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "Your Full Name"
        self.fields[
            'profile_pic'
            ].label = "Please upload a photo of yourself here! (Optional)"