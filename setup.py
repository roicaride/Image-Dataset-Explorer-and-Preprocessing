#!/usr/bin/env python3
"""
Script de configuración para Image Dataset Explorer and Preprocessing with Python
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """Verifica que la versión de Python sea compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Se requiere Python 3.8 o superior")
        print(f"   Versión actual: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detectado")
    return True

def install_requirements():
    """Instala las dependencias del proyecto"""
    print("📦 Instalando dependencias...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        return False

def create_directories():
    """Crea las carpetas necesarias si no existen"""
    directories = ["data", "notebooks", "docs", "models", "logs"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"📁 Carpeta '{directory}' creada/verificada")

def check_data_file():
    """Verifica si el archivo de datos está presente"""
    data_file = "Assignment data.zip"
    if os.path.exists(data_file):
        print(f"✅ Archivo de datos encontrado: {data_file}")
        return True
    else:
        print(f"⚠️  Archivo de datos no encontrado: {data_file}")
        print("   Por favor, coloca el archivo 'Assignment data.zip' en la raíz del proyecto")
        return False

def setup_jupyter():
    """Configura Jupyter para el proyecto"""
    print("🔧 Configurando Jupyter...")
    try:
        # Crear kernel para el proyecto
        subprocess.check_call([sys.executable, "-m", "ipykernel", "install", "--user", "--name=image-dataset-explorer"])
        print("✅ Kernel de Jupyter configurado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️  No se pudo configurar el kernel de Jupyter: {e}")
        return True  # No es crítico

def main():
    """Función principal de configuración"""
    print("🚀 Configurando Image Dataset Explorer and Preprocessing with Python")
    print("=" * 60)
    
    # Verificar versión de Python
    if not check_python_version():
        sys.exit(1)
    
    # Crear directorios
    create_directories()
    
    # Verificar archivo de datos
    check_data_file()
    
    # Instalar dependencias
    if not install_requirements():
        sys.exit(1)
    
    # Configurar Jupyter
    setup_jupyter()
    
    print("\n" + "=" * 60)
    print("✅ Configuración completada exitosamente!")
    print("\n📋 Próximos pasos:")
    print("1. Abre Jupyter Notebook: jupyter notebook")
    print("2. Navega a la carpeta 'notebooks'")
    print("3. Abre 'assignment_final.ipynb'")
    print("4. Ejecuta las celdas en orden")
    print("\n📚 Documentación disponible en:")
    print("   - README.md (guía principal)")
    print("   - docs/project_description.md (documentación detallada)")
    print("\n🎉 ¡Listo para comenzar!")

if __name__ == "__main__":
    main() 