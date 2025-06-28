# 🏥 Sistema Clínico Django - GUÍA DE INSTALACIÓN

Sistema de gestión clínica completo desarrollado en Django con funcionalidades para administración de pacientes, doctores, citas médicas, atenciones y facturación.

## 🚀 INSTALACIÓN EN MÁQUINA NUEVA

### Opción 1: Instalación Automática (⭐ RECOMENDADA)
```bash
# 1. Clonar o descargar el proyecto en tu máquina
# 2. Abrir terminal/cmd en la carpeta del proyecto
# 3. Ejecutar UN SOLO COMANDO:
python setup.py
```

### Opción 2: Instalación Manual
```bash
# 1. Instalar dependencias
pip install -r dependencias.txt

# 2. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

# 3. Configurar sistema completo
python manage.py setup_sistema --reset

# 4. Ejecutar servidor
python manage.py runserver
```

### 🌐 Acceso al Sistema
Después de cualquiera de las dos opciones:
- Abrir navegador en: `http://127.0.0.1:8000/`
- El sistema estará **100% funcional** con datos de ejemplo

---

## ✅ ¿QUÉ INSTALA AUTOMÁTICAMENTE?

### 🔒 Sistema de Seguridad Completo
- **23 Módulos** organizados por funcionalidad
- **3 Menús principales**: Core, Doctor, Seguridad  
- **4 Grupos de usuarios**: Administrador, Doctor, Recepcionista, Contador
- **44 Permisos** asignados con control granular

### 📋 Catálogos Base (Listos para usar)
- **8 Tipos de sangre**: A+, A-, B+, B-, AB+, AB-, O+, O-
- **13 Especialidades**: Cardiología, Dermatología, Pediatría, etc.
- **10 Cargos**: Director, Administrador, Recepcionista, etc.
- **15 Medicamentos**: Con marcas y tipos realistas
- **16 Diagnósticos**: Condiciones médicas comunes
- **12 Tipos de gastos**: Categorías financieras

### 👥 Datos de Ejemplo (Simulan uso real)
- **6 Pacientes** con información completa
- **4 Doctores** especialistas con horarios
- **4 Empleados** administrativos
- **26 Citas médicas** distribuidas
- **3 Atenciones** con diagnósticos y tratamientos
- **Sistema de pagos** completo
- **30 Gastos mensuales** para seguimiento financiero

---

## 🔧 COMANDOS IMPORTANTES

```bash
# Reiniciar sistema completo (⚠️ BORRA TODOS LOS DATOS)
python manage.py setup_sistema --reset

# Solo agregar datos sin borrar existentes
python manage.py setup_sistema

# Verificar que todo funciona
python manage.py check

# Crear usuario administrador
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

---

## 📁 ESTRUCTURA DEL PROYECTO

### Aplicaciones Principales
- **Core**: Pacientes, catálogos médicos, empleados, gastos
- **Doctor**: Citas médicas, atenciones, horarios, servicios, pagos
- **Security**: Usuarios, módulos, menús, grupos, permisos

### Archivos Clave
```
app_security/
├── applications/core/management/commands/setup_sistema.py  # ⭐ Comando principal
├── orms/crear_datos_completos.py                          # Script de datos
├── setup.py                                               # ⭐ Instalación automática
├── manage.py                                               # Django
└── dependencias.txt                                        # Librerías
```

---

## ⚠️ NOTAS IMPORTANTES

- **El comando `--reset` ELIMINA todos los datos existentes**
- Los datos de ejemplo son realistas pero ficticios
- El sistema está listo para uso inmediato
- Todas las relaciones y validaciones están correctas

---

## 🎉 ¡RESULTADO FINAL!

Después de ejecutar `python setup.py`:

✅ **Base de datos configurada**  
✅ **23 módulos creados**  
✅ **4 grupos con permisos**  
✅ **Datos de ejemplo cargados**  
✅ **Sistema 100% funcional**  

**Solo ejecuta `python manage.py runserver` y visita `http://127.0.0.1:8000/`**

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Si el comando falla:
```bash
# Verificar que Python esté instalado
python --version

# Verificar que las dependencias estén instaladas
pip list

# Ejecutar paso a paso manualmente
python manage.py makemigrations
python manage.py migrate
python manage.py setup_sistema --reset
```

### Para empezar de cero:
```bash
# Eliminar base de datos
del db.sqlite3
# Volver a ejecutar setup
python setup.py
```

**¡El sistema estará listo en menos de 2 minutos!** 🚀

---

# 🚀 INSTALACIÓN PASO A PASO

## ⚠️ Requisitos previos:
- Python 3.8+ instalado
- Git instalado (opcional)

## 🔧 Instalación:

### 1. Descargar el proyecto
```bash
# Opción A: Con git
git clone <tu-repositorio>
cd app_security-main

# Opción B: Descargar ZIP y extraer
```

### 2. Crear entorno virtual (OBLIGATORIO)
```bash
python -m venv venv
```

### 3. Activar entorno virtual (OBLIGATORIO)
```bash
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 4. Instalación automática (TODO EN UNO)
```bash
python setup.py
```

### 5. Ejecutar servidor
```bash
python manage.py runserver
```

## ✅ ¡Listo! Visita: http://127.0.0.1:8000/
