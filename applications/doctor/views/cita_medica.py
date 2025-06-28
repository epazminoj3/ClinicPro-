from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import CitaMedica
from applications.doctor.forms import CitaMedicaForm


# ==================== VISTAS DE CITA MEDICA ====================
class CitaMedicaListView(ListView):
    model = CitaMedica
    template_name = 'doctor/cita_medica/list.html'
    context_object_name = 'citas'
    paginate_by = 10

    def get_queryset(self):
        return CitaMedica.objects.all().order_by('fecha', 'hora_cita')


class CitaMedicaCreateView(CreateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'doctor/cita_medica/form.html'
    success_url = reverse_lazy('doctor:cita_list')


class CitaMedicaUpdateView(UpdateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'doctor/cita_medica/form.html'
    success_url = reverse_lazy('doctor:cita_list')


class CitaMedicaDeleteView(DeleteView):
    model = CitaMedica
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('doctor:cita_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cita Médica'
        context['question'] = f'¿Está seguro de eliminar la cita de {self.object.paciente} el {self.object.fecha} a las {self.object.hora_cita}?'
        context['cancel_url'] = self.success_url
        return context
