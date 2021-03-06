from django.shortcuts import render, redirect
from .models import Cocktail


def index(request):
    if request.method == 'POST':
        cocktail_name = request.POST.get('name', '')
        if cocktail_name:
            cocktail = Cocktail.objects.create(
                name=cocktail_name
                )
            cocktail.save()
        print(cocktail_name)
        return redirect('/bar')

    cocktails = Cocktail.objects.all()
    context = {'data': 'this is your bar!', 'cocktails': cocktails}
    return render(request, 'bar/index.html', context)
