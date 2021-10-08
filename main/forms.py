from django import forms
from .models import messages, requests

class commentAdd(forms.ModelForm):
    class Meta:
        model = messages
        fields = ['mess']
        labels = {'mess':"コメント"}

class postForm(forms.ModelForm):
    class Meta:
        model = requests
        fields = ['title', 'text', 'departure_place', 'destination_place', 'delivery_date', 'asking_price']
        labels ={
            'title':"タイトル",
            'text':"内容",
            'departure_place':"出発地",
            'destination_place':"目的地",
            'delivery_date':"配達日",
            'asking_price':"希望価格(円)"
        }