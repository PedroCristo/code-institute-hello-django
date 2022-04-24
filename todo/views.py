
# We use the HttpResponse if we write a string in the function
# from django.shortcuts import render, HttpResponse

from django.shortcuts import render

# Create your views here.

def get_todo_nav(request):
    return render(request, 'todo/todo_list.html')

