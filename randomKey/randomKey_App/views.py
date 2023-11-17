from django.shortcuts import render
import random
from .models import Keyrecord

def index(request):
    characters=list('abcdefghijklmnoprstuvyzxw123456789!%&/()?')
    random_key=''
    lenght =9
    for i in range(lenght):
        random_key += random.choice(characters)
        
    generate_entry = Keyrecord(key=random_key)
    generate_entry.save()
    return render(request, 'index.html', {'random_Key':random_key})
