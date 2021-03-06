from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        print(request.POST.get('url'))
    context = {'data': 'this is your bar!'}
    return render(request, 'bar/index.html', context)
