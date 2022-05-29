from django.shortcuts import render
from passagens.forms import PassagemForm


def index(request):
    form = PassagemForm
    context = {'form': form}
    return render(request, 'home.html', context)


def detalhes(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        if form.is_valid():
            context = {'form': form}
            return render(request, 'detalhes.html', context)
        return render(request, 'home.html', {'form': form})
