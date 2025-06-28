from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Medicamento, TipoMedicamento, MarcaMedicamento
from applications.core.forms import MedicamentoForm, TipoMedicamentoForm, MarcaMedicamentoForm


# ==================== VISTAS DE MEDICAMENTO ====================
class MedicamentoListView(ListView):
    model = Medicamento
    template_name = 'core/medicamento/list.html'
    context_object_name = 'medicamentos'
    paginate_by = 10

    def get_queryset(self):
        return Medicamento.objects.filter(activo=True).order_by('nombre')


class MedicamentoCreateView(CreateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('core:medicamento_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'core/medicamento/form.html'
    success_url = reverse_lazy('core:medicamento_list')


class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Medicamento'
        context['question'] = f'¿Está seguro de eliminar el medicamento {self.object.nombre}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE TIPO MEDICAMENTO ====================
class TipoMedicamentoListView(ListView):
    model = TipoMedicamento
    template_name = 'core/tipo_medicamento/list.html'
    context_object_name = 'tipos'
    paginate_by = 10

    def get_queryset(self):
        return TipoMedicamento.objects.filter(activo=True).order_by('nombre')


class TipoMedicamentoCreateView(CreateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core/tipo_medicamento/form.html'
    success_url = reverse_lazy('core:tipo_medicamento_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class TipoMedicamentoUpdateView(UpdateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core/tipo_medicamento/form.html'
    success_url = reverse_lazy('core:tipo_medicamento_list')


class TipoMedicamentoDeleteView(DeleteView):
    model = TipoMedicamento
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:tipo_medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Tipo de Medicamento'
        context['question'] = f'¿Está seguro de eliminar el tipo {self.object.nombre}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE MARCA MEDICAMENTO ====================
class MarcaMedicamentoListView(ListView):
    model = MarcaMedicamento
    template_name = 'core/marca_medicamento/list.html'
    context_object_name = 'marcas'
    paginate_by = 10

    def get_queryset(self):
        return MarcaMedicamento.objects.filter(activo=True).order_by('nombre')


class MarcaMedicamentoCreateView(CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core/marca_medicamento/form.html'
    success_url = reverse_lazy('core:marca_medicamento_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class MarcaMedicamentoUpdateView(UpdateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core/marca_medicamento/form.html'
    success_url = reverse_lazy('core:marca_medicamento_list')


class MarcaMedicamentoDeleteView(DeleteView):
    model = MarcaMedicamento
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:marca_medicamento_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Marca de Medicamento'
        context['question'] = f'¿Está seguro de eliminar la marca {self.object.nombre}?'
        context['cancel_url'] = self.success_url
        return context