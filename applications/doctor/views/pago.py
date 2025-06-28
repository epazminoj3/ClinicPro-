from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.models import Pago, DetallePago
from applications.doctor.forms import PagoForm, DetallePagoForm


# ==================== VISTAS DE PAGO ====================
class PagoListView(ListView):
    model = Pago
    template_name = 'doctor/pago/list.html'
    context_object_name = 'pagos'
    paginate_by = 10

    def get_queryset(self):
        return Pago.objects.filter(activo=True).order_by('-fecha_creacion')


class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pago/form.html'
    success_url = reverse_lazy('doctor:pago_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pago/form.html'
    success_url = reverse_lazy('doctor:pago_list')


class PagoDeleteView(DeleteView):
    model = Pago
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('doctor:pago_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Pago'
        context['question'] = f'¿Está seguro de eliminar el pago #{self.object.id} por ${self.object.monto_total}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE DETALLE PAGO ====================
class DetallePagoListView(ListView):
    model = DetallePago
    template_name = 'doctor/detalle_pago/list.html'
    context_object_name = 'detalles'
    paginate_by = 10

    def get_queryset(self):
        return DetallePago.objects.all().order_by('-pago__fecha_creacion')


class DetallePagoCreateView(CreateView):
    model = DetallePago
    form_class = DetallePagoForm
    template_name = 'doctor/detalle_pago/form.html'
    success_url = reverse_lazy('doctor:detalle_pago_list')


class DetallePagoUpdateView(UpdateView):
    model = DetallePago
    form_class = DetallePagoForm
    template_name = 'doctor/detalle_pago/form.html'
    success_url = reverse_lazy('doctor:detalle_pago_list')


class DetallePagoDeleteView(DeleteView):
    model = DetallePago
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('doctor:detalle_pago_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Detalle de Pago'
        context['question'] = f'¿Está seguro de eliminar el detalle {self.object.servicio_adicional} del pago #{self.object.pago.id}?'
        context['cancel_url'] = self.success_url
        return context
