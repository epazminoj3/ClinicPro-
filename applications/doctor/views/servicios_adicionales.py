from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import ServiciosAdicionales
from applications.doctor.forms import ServiciosAdicionalesForm


# ==================== VISTAS DE SERVICIOS ADICIONALES ====================
class ServiciosAdicionalesListView(ListView):
    model = ServiciosAdicionales
    template_name = 'doctor/servicios_adicionales/list.html'
    context_object_name = 'servicios'
    paginate_by = 10

    def get_queryset(self):
        return ServiciosAdicionales.objects.filter(activo=True).order_by('nombre_servicio')


class ServiciosAdicionalesCreateView(CreateView):
    model = ServiciosAdicionales
    form_class = ServiciosAdicionalesForm
    template_name = 'doctor/servicios_adicionales/form.html'
    success_url = reverse_lazy('doctor:servicios_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class ServiciosAdicionalesUpdateView(UpdateView):
    model = ServiciosAdicionales
    form_class = ServiciosAdicionalesForm
    template_name = 'doctor/servicios_adicionales/form.html'
    success_url = reverse_lazy('doctor:servicios_list')


class ServiciosAdicionalesDeleteView(DeleteView):
    model = ServiciosAdicionales
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('doctor:servicios_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Servicio Adicional'
        context['question'] = f'¿Está seguro de eliminar el servicio {self.object.nombre_servicio}?'
        context['cancel_url'] = self.success_url
        return context
