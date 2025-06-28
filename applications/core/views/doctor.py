from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Doctor, Especialidad
from applications.core.forms import DoctorForm, EspecialidadForm


# ==================== VISTAS DE DOCTOR ====================
class DoctorListView(ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctores'
    paginate_by = 10

    def get_queryset(self):
        return Doctor.objects.filter(activo=True).order_by('nombres')


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:doctor_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Doctor'
        context['question'] = f'¿Está seguro de eliminar al doctor {self.object.nombres} {self.object.apellidos}?'
        context['cancel_url'] = self.success_url
        return context


# ==================== VISTAS DE ESPECIALIDAD ====================
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'core/especialidad/list.html'
    context_object_name = 'especialidades'
    paginate_by = 10

    def get_queryset(self):
        return Especialidad.objects.filter(activo=True).order_by('nombre')


class EspecialidadCreateView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'core/especialidad/form.html'
    success_url = reverse_lazy('core:especialidad_list')

    def form_valid(self, form):
        form.instance.activo = True
        return super().form_valid(form)


class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'core/especialidad/form.html'
    success_url = reverse_lazy('core:especialidad_list')


class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'fragments/delete.html'
    success_url = reverse_lazy('core:especialidad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Especialidad'
        context['question'] = f'¿Está seguro de eliminar la especialidad {self.object.nombre}?'
        context['cancel_url'] = self.success_url
        return context