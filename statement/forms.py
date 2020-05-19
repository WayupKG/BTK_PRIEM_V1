from django.forms import ModelForm, TextInput, Textarea, FileInput, DateInput
from .models import *


class StatementForm(ModelForm):
    class Meta:
        model = Statement
        fields = ['first_name',
                  'last_name',
                  'patronymic',
                  'graduated',
                  'near',
                  'certificate_number',
                  'certificate_date',
                  'date_of_birth',
                  'nationality',
                  'passport_or_certificate',
                  'floor',
                  'specialty',
                  'father',
                  'father_phone',
                  'mother',
                  'mother_phone',
                  'place_of_residence',
                  'phone_student',
                  'image_student',
                  'image_certificate',
                  'image_passport_or_certificate']
        widgets = {
            'date_of_birth': DateInput(attrs={
                'type': 'date',
                'class': 'red',
            })
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'id': "exampleFormControlTextarea1",
                "rows": "3",
            })
        }
