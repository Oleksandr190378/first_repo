from django.forms import ModelForm, CharField, TextInput, ModelChoiceField,ModelMultipleChoiceField,Form
from .models import Author, Quote
from django import forms

class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=150, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())


    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.Form):
    quote = forms.CharField(min_length=5, required=True, widget=TextInput())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), to_field_name='fullname', empty_label=None,)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].label_from_instance = lambda obj: obj.fullname






