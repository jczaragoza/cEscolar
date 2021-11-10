from django.shortcuts import render
from django.views.generic import ListView

from core.erp.models import Categorias


def categoria_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Categorias.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoriaListView(ListView):
    model = Categorias
    template_name = 'category/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
