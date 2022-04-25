
# We use the HttpResponse if we write a string in the function
# from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Item
from .forms import itemForm


# Create your views here.
def get_todo_nav(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_nav')
    form = itemForm()
    context = {
            'form': form
    }

    return render(request, 'todo/add_item.html', context)

