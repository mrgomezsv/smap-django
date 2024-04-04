from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'featured_image', 'description', 'additional_images']

    widgets = {
        'featured_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    }