from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from .models import Sushi
import random

def random_sushi(request):
    sushi_list = Sushi.objects.all()
    selected_sushi = random.choice(sushi_list) if sushi_list else None
    return render(request, 'random_sushi.html', {'sushi': selected_sushi})
