from django.forms import ModelForm, TextInput, Textarea, FileInput
from .models import Specialty


class SpecialtyForm(ModelForm):

    class Meta:
        model = Specialty
        fields = ['title', 'body', 'img']
        widgets = {'title': TextInput(attrs={
            'name': 'title',
            'placeholder': 'Называние',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Называние"',
            'class': 'single-input-primary Specialty'
        }),

            'body': Textarea(attrs={
                'name': 'body',
                'cols': '80',
                'rows': '40',
                'placeholder': 'Описание',
                'onfocus': 'this.placeholder = ""',
                'onblur': 'this.placeholder = "Описание"',
                'class': 'single-input-primary Specialty SpecialtyTextarea'
            }),

        }
