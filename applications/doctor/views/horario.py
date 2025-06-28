from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import HorarioAtencion
from applications.doctor.forms import HorarioAtencionForm


# ==================== VISTAS DE HORARIO DE ATENCION ====================
class HorarioAtencionListView(ListView):
    model = HorarioAtencion
    template_name = 'doctor/horario/list.html'
    context_object_name = 'horarios'
    paginate_by = 10

    def get_queryset(self):
        return HorarioAtencion.objects.filter(activo=True).order_by('dia_semana', 'hora_inicio')


class HorarioAtencionCreateView(CreateView):
    model = HorarioAtencion
    form_class = HorarioAtencionForm
    template_name = 'doctor/horario/form.html'
    success_url = reverse_lazy('doctor:horario_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class HorarioAtencionUpdateView(UpdateView):
    model = HorarioAtencion
    form_class = HorarioAtencionForm
    template_name = 'doctor/horario/form.html'
    success_url = reverse_lazy('doctor:horario_list')


class HorarioAtencionDeleteView(DeleteView):
    model = HorarioAtencion
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('doctor:horario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Horario'
        context['question'] = f'¿Está seguro de eliminar el horario {self.object.dia_semana} {self.object.hora_inicio}-{self.object.hora_fin}?'
        context['cancel_url'] = self.success_url
        return context
