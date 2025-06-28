from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Paciente
from applications.core.forms import PacienteForm


class PacienteListView(ListView):
    model = Paciente
    template_name = 'core/paciente/list.html'
    context_object_name = 'pacientes'
    paginate_by = 10

    def get_queryset(self):
        return Paciente.objects.filter(activo=True).order_by('apellidos', 'nombres')


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/create.html'
    success_url = reverse_lazy('core:paciente_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/create.html'
    success_url = reverse_lazy('core:paciente_list')


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:paciente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Paciente'
        context['question'] = f'¿Está seguro de eliminar al paciente {self.object.nombres} {self.object.apellidos}?'
        context['cancel_url'] = self.success_url
        return context