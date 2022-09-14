from django.shortcuts import render


posts = [
    {
        'author': 'QRage',
        'title': 'News Post 1',
        'content': 'First post content',
        'date_posted': 'September 12, 2022'
    },
    {
        'author': 'John Doe',
        'title': 'News Post 2',
        'content': 'Second post content',
        'date_posted': 'September 13, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'news/home.html', context)


def about(request):
    return render(request, 'news/about.html', {'title': 'About'})
