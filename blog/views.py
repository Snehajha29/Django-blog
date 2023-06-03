from django.shortcuts import render

STUDENTS = [
    {
        'first_name': 'Sneha',
        'last_names': '',
    }
]

def home(request):
    return render(request, 'blog/home.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

