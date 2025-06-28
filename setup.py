#!/usr/bin/env python
"""
Script de instalación automática del Sistema Clínico
Configura todo el proyecto de cero incluyendo:
- Dependencias
- Base de datos
- Módulos y permisos
- Datos de ejemplo
"""

import os
import sys
import subprocess
import platform

def ejecutar_comando(comando, descripcion=""):
    """Ejecuta un comando y muestra el resultado"""
    if descripcion:
        print(f"🔧 {descripcion}")
    
    print(f"   Ejecutando: {comando}")
    
    try:
        resultado = subprocess.run(
            comando, 
            shell=True, 
            capture_output=True, 
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        
        if resultado.returncode == 0:
            print(f"   ✅ Completado exitosamente")
            return True
        else:
            print(f"   ❌ Error: {resultado.stderr}")
            return False
            
    except Exception as e:
        print(f"   ❌ Excepción: {str(e)}")
        return False

def verificar_python():
    """Verifica que Python esté instalado"""
    print("🐍 Verificando Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Se requiere Python 3.8+, encontrado: {version.major}.{version.minor}")
        return False

def crear_entorno_virtual():
    """Crea y activa entorno virtual"""
    print("📦 Configurando entorno virtual...")
    
    if os.path.exists('venv'):
        print("   ⚠️  Entorno virtual ya existe")
        return True
    
    if not ejecutar_comando("python -m venv venv", "Creando entorno virtual"):
        return False
    
    print("   ✅ Entorno virtual creado")
    return True

def activar_entorno():
    """Retorna el comando para activar el entorno virtual"""
    sistema = platform.system()
    if sistema == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def instalar_dependencias():
    """Instala dependencias del proyecto"""
    print("📚 Instalando dependencias...")
    
    # Comando según el sistema operativo
    if platform.system() == "Windows":
        comando = "venv\\Scripts\\pip install -r requirements.txt"
    else:
        comando = "venv/bin/pip install -r requirements.txt"
    
    return ejecutar_comando(comando, "Instalando paquetes Python")

def configurar_base_datos():
    """Aplica migraciones"""
    print("🗄️  Configurando base de datos...")
    
    # Comando según el sistema operativo
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
    else:
        python_cmd = "venv/bin/python"
    
    if not ejecutar_comando(f"{python_cmd} manage.py makemigrations", "Generando migraciones"):
        return False
    
    if not ejecutar_comando(f"{python_cmd} manage.py migrate", "Aplicando migraciones"):
        return False
    
    return True

def instalar_datos_sistema():
    """Instala módulos, grupos, permisos y datos de ejemplo"""
    print("🏥 Instalando datos del sistema...")
    
    # Comando según el sistema operativo
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
    else:
        python_cmd = "venv/bin/python"
    
    return ejecutar_comando(
        f"{python_cmd} manage.py setup_sistema", 
        "Instalando módulos, grupos, permisos y datos de ejemplo"
    )

def mostrar_instrucciones_finales():
    """Muestra instrucciones para usar el sistema"""
    print("\n" + "=" * 60)
    print("🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!")
    print("=" * 60)
    print()
    print("📋 PRÓXIMOS PASOS:")
    print()
    
    sistema = platform.system()
    if sistema == "Windows":
        print("1. Activar entorno virtual:")
        print("   venv\\Scripts\\activate")
        print()
        print("2. Ejecutar servidor:")
        print("   python manage.py runserver")
    else:
        print("1. Activar entorno virtual:")
        print("   source venv/bin/activate")
        print()
        print("2. Ejecutar servidor:")
        print("   python manage.py runserver")
    
    print()
    print("3. Abrir navegador en:")
    print("   http://127.0.0.1:8000/")
    print()
    print("🔗 ENLACES PRINCIPALES:")
    print("   📋 Pacientes: http://127.0.0.1:8000/core/paciente/")
    print("   👨‍⚕️ Doctores: http://127.0.0.1:8000/core/doctor/")
    print("   📅 Citas: http://127.0.0.1:8000/doctor/cita_medica/")
    print("   🩺 Atenciones: http://127.0.0.1:8000/doctor/atencion/")
    print("   💳 Pagos: http://127.0.0.1:8000/doctor/pago/")
    print()
    print("👥 GRUPOS CREADOS:")
    print("   • Administradores (acceso completo)")
    print("   • Médicos (acceso a atenciones y pacientes)")
    print("   • Asistentes (acceso limitado)")
    print("   • Recepcionistas (citas y pagos)")
    print()
    print("📊 DATOS DE EJEMPLO:")
    print("   • 6 pacientes con historias clínicas")
    print("   • 4 doctores con especialidades")
    print("   • 15 medicamentos")
    print("   • 15 diagnósticos")
    print("   • 27 citas médicas")
    print("   • 6 atenciones con recetas")
    print("   • Servicios y pagos")
    print()
    print("🔄 Para reinstalar datos:")
    print("   python manage.py setup_sistema --reset")

def main():
    """Función principal de instalación"""
    print("🏥 INSTALADOR DEL SISTEMA CLÍNICO")
    print("=" * 60)
    print("Este script configurará todo el sistema automáticamente")
    print()
    
    # Verificar requisitos
    if not verificar_python():
        print("❌ Instalación abortada: Python no cumple requisitos")
        return False
    
    if not os.path.exists('requirements.txt'):
        print("❌ Error: No se encontró requirements.txt")
        return False
    
    if not os.path.exists('manage.py'):
        print("❌ Error: No se encontró manage.py")
        return False
    
    # Proceso de instalación
    pasos = [
        (crear_entorno_virtual, "Crear entorno virtual"),
        (instalar_dependencias, "Instalar dependencias"),
        (configurar_base_datos, "Configurar base de datos"),
        (instalar_datos_sistema, "Instalar datos del sistema"),
    ]
    
    print("🚀 Iniciando instalación...")
    print()
    
    for paso_func, descripcion in pasos:
        if not paso_func():
            print(f"\n❌ Error en: {descripcion}")
            print("💡 Revise los mensajes de error anteriores")
            return False
        print()
    
    # Éxito
    mostrar_instrucciones_finales()
    return True

if __name__ == "__main__":
    try:
        exito = main()
        if not exito:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n⚠️  Instalación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")
        sys.exit(1)
