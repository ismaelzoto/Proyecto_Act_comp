from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.crud_alumnos.models import alumnos,estado
from apps.crud_alumnos.forms import alumnosForm,estadoForm
from apps.crud_alumnos.filters import alumnosFilter,estadoFilter
from django.urls import reverse_lazy
# Create your views here.


class alumnosCreate(CreateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudalumnos/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')


class alumnosList(ListView):
    queryset = alumnos.objects.order_by('nocontrol')
    template_name = 'crudalumnos/alumnos_list.html'
    paginate_by = 5


class alumnosUpdate(UpdateView):
    model = alumnos
    form_class = alumnosForm
    template_name = 'crudalumnos/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')


class alumnosDelete(DeleteView):
    model = alumnos
    template_name = 'crudalumnos/alumnos_delete.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')


class alumnoShow(DetailView):
    model = alumnos
    template_name = 'crudalumnos/alumno_show.html'

# buscar o filtrar
# Para agregar la vista de búsqueda, se instala primero
# pip install django-filters
def search(request):
    alumnos_list = alumnos.objects.all()
    alumnos_filter = alumnosFilter(request.GET, queryset=alumnos_list)
    return render(request, 'crudalumnos/alumnos_list_filter.html', {'filter': alumnos_filter})
#aqui inicia la vista del crud estado
class estadoCreate(CreateView):
    model = estado
    form_class = estadoForm
    template_name = 'crudalumnos/estados_form.html'
    success_url = reverse_lazy('estados:estado_lista')


class estadoList(ListView):
    queryset = estado.objects.order_by('id_estado')
    template_name = 'crudalumnos/estados_list.html'
    paginate_by = 10


class estadoUpdate(UpdateView):
    model = estado
    form_class = estadoForm
    template_name = 'crudalumnos/estados_form.html'
    success_url = reverse_lazy('estados:estado_lista')


class estadoDelete(DeleteView):
    model = estado
    template_name = 'crudalumnos/estados_delete.html'
    success_url = reverse_lazy('estados:estado_lista')


class estadoShow(DetailView):
    model = estado
    template_name = 'crudalumnos/estado_show.html'

def search_c(request):
    estado_list = estado.objects.all()
    estado_filter = estadoFilter(request.GET, queryset=estado_list)
    return render(request, 'crudalumnos/estados_list_filter.html', {'filter': estado_filter})
