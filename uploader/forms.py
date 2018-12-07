from django import forms

class UploadForm(forms.Form):
    # email = forms.EmailField(label='Email link to', help_text='(Optional)', required=False)
    file = forms.FileField(required=True)
