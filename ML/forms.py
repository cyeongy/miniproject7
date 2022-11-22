from django import forms
from .models import ML_Model

class MakeMLModelForm(forms.ModelForm):
    class Meta:
        model = ML_Model
        fields = ['title', 'version', 'is_selected', 'model_file'] 