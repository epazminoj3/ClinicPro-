from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import (
    Empleado, Cargo, Diagnostico, TipoGasto, 
    GastoMensual, TipoSangre
)
from applications.core.forms import (
    EmpleadoForm, CargoForm, DiagnosticoForm, 
    TipoGastoForm, GastoMensualForm, TipoSangreForm
)


# ==================== VISTAS DE EMPLEADO ====================
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'core/empleado/list.html'
    context_object_name = 'empleados'
    paginate_by = 10

    def get_queryset(self):
        return Empleado.objects.filter(activo=True).order_by('nombres')


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core/empleado/form.html'
    success_url = reverse_lazy('core:empleado_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core/empleado/form.html'
    success_url = reverse_lazy('core:empleado_list')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:empleado_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Empleado'
        context['question'] = f'¿Está seguro de eliminar al empleado {self.object.nombres} {self.object.apellidos}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE CARGO ====================
class CargoListView(ListView):
    model = Cargo
    template_name = 'core/cargo/list.html'
    context_object_name = 'cargos'
    paginate_by = 10

    def get_queryset(self):
        return Cargo.objects.filter(activo=True).order_by('nombre')


class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'core/cargo/form.html'
    success_url = reverse_lazy('core:cargo_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'core/cargo/form.html'
    success_url = reverse_lazy('core:cargo_list')


class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:cargo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cargo'
        context['question'] = f'¿Está seguro de eliminar el cargo {self.object.nombre}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE DIAGNOSTICO ====================
class DiagnosticoListView(ListView):
    model = Diagnostico
    template_name = 'core/diagnostico/list.html'
    context_object_name = 'diagnosticos'
    paginate_by = 10

    def get_queryset(self):
        return Diagnostico.objects.filter(activo=True).order_by('codigo')


class DiagnosticoCreateView(CreateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'core/diagnostico/form.html'
    success_url = reverse_lazy('core:diagnostico_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class DiagnosticoUpdateView(UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'core/diagnostico/form.html'
    success_url = reverse_lazy('core:diagnostico_list')


class DiagnosticoDeleteView(DeleteView):
    model = Diagnostico
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:diagnostico_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Diagnóstico'
        context['question'] = f'¿Está seguro de eliminar el diagnóstico {self.object.codigo} - {self.object.descripcion}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE TIPO GASTO ====================
class TipoGastoListView(ListView):
    model = TipoGasto
    template_name = 'core/tipo_gasto/list.html'
    context_object_name = 'tipos'
    paginate_by = 10

    def get_queryset(self):
        return TipoGasto.objects.filter(activo=True).order_by('nombre')


class TipoGastoCreateView(CreateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'core/tipo_gasto/form.html'
    success_url = reverse_lazy('core:tipo_gasto_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class TipoGastoUpdateView(UpdateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'core/tipo_gasto/form.html'
    success_url = reverse_lazy('core:tipo_gasto_list')


class TipoGastoDeleteView(DeleteView):
    model = TipoGasto
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:tipo_gasto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Tipo de Gasto'
        context['question'] = f'¿Está seguro de eliminar el tipo {self.object.nombre}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE GASTO MENSUAL ====================
class GastoMensualListView(ListView):
    model = GastoMensual
    template_name = 'core/gasto_mensual/list.html'
    context_object_name = 'gastos'
    paginate_by = 10

    def get_queryset(self):
        return GastoMensual.objects.all().order_by('-fecha')


class GastoMensualCreateView(CreateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gasto_mensual/form.html'
    success_url = reverse_lazy('core:gasto_mensual_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class GastoMensualUpdateView(UpdateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gasto_mensual/form.html'
    success_url = reverse_lazy('core:gasto_mensual_list')


class GastoMensualDeleteView(DeleteView):
    model = GastoMensual
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:gasto_mensual_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Gasto'
        context['question'] = f'¿Está seguro de eliminar este gasto?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE TIPO SANGRE ====================
class TipoSangreListView(ListView):
    model = TipoSangre
    template_name = 'core/tipo_sangre/list.html'
    context_object_name = 'tipos'
    paginate_by = 10

    def get_queryset(self):
        return TipoSangre.objects.all().order_by('tipo')


class TipoSangreCreateView(CreateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tipo_sangre/form.html'
    success_url = reverse_lazy('core:tipo_sangre_list')


class TipoSangreUpdateView(UpdateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tipo_sangre/form.html'
    success_url = reverse_lazy('core:tipo_sangre_list')


class TipoSangreDeleteView(DeleteView):
    model = TipoSangre
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:tipo_sangre_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Tipo de Sangre'
        context['question'] = f'¿Está seguro de eliminar el tipo {self.object.tipo}?'
        context['cancel_url'] = self.success_url
        return context