
# We use the HttpResponse if we write a string in the function
# from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_nav(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
