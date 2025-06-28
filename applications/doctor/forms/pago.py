from django import forms
from applications.doctor.models import Pago, DetallePago


class PagoForm(forms.ModelForm):
    """Formulario para crear y editar pagos"""
    
    class Meta:
        model = Pago
        fields = [
            'atencion', 'metodo_pago', 'monto_total', 'estado', 'fecha_pago',
            'nombre_pagador', 'referencia_externa', 'evidencia_pago', 'observaciones'
        ]
        widgets = {
            'atencion': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
            }),
            'metodo_pago': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
            }),
            'monto_total': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'step': '0.01',
                'min': 0
            }),
            'estado': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
            }),
            'fecha_pago': forms.DateTimeInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'type': 'datetime-local'
            }),
            'nombre_pagador': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'Nombre de quien paga'
            }),
            'referencia_externa': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'ID de transacción PayPal, etc.'
            }),
            'evidencia_pago': forms.FileInput(attrs={
                'class': 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'rows': 3,
                'placeholder': 'Observaciones adicionales...'
            }),
        }


class DetallePagoForm(forms.ModelForm):
    """Formulario para crear y editar detalles de pago"""
    
    class Meta:
        model = DetallePago
        fields = [
            'pago', 'servicio_adicional', 'cantidad', 'precio_unitario', 
            'descuento_porcentaje', 'aplica_seguro', 'valor_seguro', 'descripcion_seguro'
        ]
        widgets = {
            'pago': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
            }),
            'servicio_adicional': forms.Select(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'min': 1
            }),
            'precio_unitario': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'step': '0.01',
                'min': 0
            }),
            'descuento_porcentaje': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'step': '0.01',
                'min': 0,
                'max': 100
            }),
            'aplica_seguro': forms.CheckboxInput(attrs={
                'class': 'mt-1 h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded'
            }),
            'valor_seguro': forms.NumberInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'step': '0.01',
                'min': 0
            }),
            'descripcion_seguro': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'Saludsa Nivel 2, etc.'
            }),
        }
