# Importar todas las vistas para disponibilizarlas en el paquete
from .atencion_medica import *
from .horario import (
    HorarioAtencionListView, HorarioAtencionCreateView, 
    HorarioAtencionUpdateView, HorarioAtencionDeleteView
)
from .cita_medica import (
    CitaMedicaListView, CitaMedicaCreateView,
    CitaMedicaUpdateView, CitaMedicaDeleteView
)
from .detalle_atencion import (
    DetalleAtencionListView, DetalleAtencionCreateView,
    DetalleAtencionUpdateView, DetalleAtencionDeleteView
)
from .servicios_adicionales import (
    ServiciosAdicionalesListView, ServiciosAdicionalesCreateView,
    ServiciosAdicionalesUpdateView, ServiciosAdicionalesDeleteView
)
from .pago import (
    PagoListView, PagoCreateView, PagoUpdateView, PagoDeleteView,
    DetallePagoListView, DetallePagoCreateView, DetallePagoUpdateView, DetallePagoDeleteView
)