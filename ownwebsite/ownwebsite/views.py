from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def education(request):
    context = {}
    return render(request, 'education.html', context)


def work(request):
    context = {}
    return render(request, 'work.html', context)


def interests(request):
    context = {}
    return render(request, 'interests.html', context)


