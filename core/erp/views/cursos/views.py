from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import CursoForm
from core.erp.models import Cursos


class CursoListView(ListView):
    model = Cursos
    template_name = 'cursos/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cursos'
        context['create_url'] = reverse_lazy('erp:curso_create')
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['entity'] = 'Cursos'
        return context


class CursoCreateView(CreateView):
    model = Cursos
    form_class = CursoForm
    template_name = 'cursos/create.html'
    success_url = reverse_lazy('erp:curso_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['action'] = 'add'
        return context


class CursoUpdateView(UpdateView):
    model = Cursos
    form_class = CursoForm
    template_name = 'cursos/create.html'
    success_url = reverse_lazy('erp:curso_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('erp:curso_list')
        context['action'] = 'edit'
        return context


class CursoDeleteView(DeleteView):
    model = Cursos
    template_name = 'cursos/delete.html'
    success_url = reverse_lazy('erp:curso_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Curso'
        context['entity'] = 'Cursos'
        context['list_url'] = reverse_lazy('erp:curso_list')
        return context
