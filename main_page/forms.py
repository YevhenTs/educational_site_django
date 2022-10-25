from django import forms
from manager.models import UserReservations

class UserReservationsForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': "form-control",
            'id': "name",
            'placeholder': "Ваше ім'я",
            'data-rule': "minlen:4",
            'data-msg': "Please enter at least 4 chars",
        }))

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'phone',
            'class': "form-control",
            'id': "phone",
            'placeholder': "Телефон",
            'data-rule': "minlen:4",
            'required': 'required',
            'data-msg': "Please enter at least 4 chars",
        }))

    persons = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': 'number',
            'name': 'people',
            'class': "form-control",
            'id': "people",
            'placeholder': "Кількість людей",
            'data-rule': "minlen:1",
            'data-msg': "Please enter at least 1 chars",
        }))

    message = forms.CharField(
        max_length=400,
        widget=forms.Textarea(attrs={
            'type': 'message',
            'name': 'message',
            'class': "form-control",
            'rows': "5",
            'placeholder': "Повідомлення",
            'required': 'required',
        }))

    class Meta:
        model = UserReservations
        fields = ('name', 'persons', 'phone', 'message')


