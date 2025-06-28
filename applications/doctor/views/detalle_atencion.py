from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import DetalleAtencion
from applications.doctor.forms import DetalleAtencionForm


# ==================== VISTAS DE DETALLE ATENCION ====================
class DetalleAtencionListView(ListView):
    model = DetalleAtencion
    template_name = 'doctor/detalle_atencion/list.html'
    context_object_name = 'detalles'
    paginate_by = 10

    def get_queryset(self):
        return DetalleAtencion.objects.all().order_by('-atencion__fecha_atencion')


class DetalleAtencionCreateView(CreateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/detalle_atencion/form.html'
    success_url = reverse_lazy('doctor:detalle_atencion_list')


class DetalleAtencionUpdateView(UpdateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/detalle_atencion/form.html'
    success_url = reverse_lazy('doctor:detalle_atencion_list')


class DetalleAtencionDeleteView(DeleteView):
    model = DetalleAtencion
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('doctor:detalle_atencion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Detalle de Atención'
        context['question'] = f'¿Está seguro de eliminar el medicamento {self.object.medicamento} de la atención de {self.object.atencion.paciente}?'
        context['cancel_url'] = self.success_url
        return context
