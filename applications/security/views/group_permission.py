from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.group_permission import GroupModulePermissionForm
from applications.security.models import Menu, Module, User, GroupModulePermission
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ================================
# VISTAS PARA GROUP MODULE PERMISSION
# ================================

class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/group_permissions/list.html'
    model = GroupModulePermission
    context_object_name = 'group_permissions'
    permission_required = 'view_groupmodulepermission'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(group__name__icontains=q1), Q.OR)
            self.query.add(Q(module__name__icontains=q1), Q.OR)
            self.query.add(Q(module__menu__name__icontains=q1), Q.OR)

        return self.model.objects.select_related('group', 'module', 'module__menu').filter(self.query).order_by('module__menu__order', 'module__order', 'group__name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:group_permission_create')
        return context


class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GroupModulePermission
    template_name = 'security/group_permissions/form.html'
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_permission_list')
    permission_required = 'add_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Permisos de Grupo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group_permission = self.object
        messages.success(self.request, f"Éxito al crear los permisos para {group_permission.group.name} - {group_permission.module.name}.")
        return response


class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = 'security/group_permissions/form.html'
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_permission_list')
    permission_required = 'change_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Permisos de Grupo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group_permission = self.object
        messages.success(self.request, f"Éxito al actualizar los permisos para {group_permission.group.name} - {group_permission.module.name}.")
        return response


class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:group_permission_list')
    permission_required = 'delete_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Permisos de Grupo'
        context['description'] = f"¿Desea eliminar los permisos de: {self.object.group.name} - {self.object.module.name}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        group_name = self.object.group.name
        module_name = self.object.module.name
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar los permisos de {group_name} - {module_name}.")
        return response