# Explorador y Preprocesamiento de Datasets de Imágenes con Python

## 📋 Descripción

Este proyecto implementa un sistema completo para la exploración y preprocesamiento de datasets de imágenes, específicamente diseñado para tareas de detección de bordes (edge detection). El proyecto incluye:

- **Preprocesamiento de imágenes**: Carga, redimensionamiento y normalización de imágenes
- **Procesamiento de datos de ground truth**: Extracción de máscaras de bordes desde archivos .mat
- **Arquitectura U-Net**: Implementación de una red neuronal convolucional para detección de bordes
- **Análisis exploratorio**: Visualización y estadísticas del dataset

## 🚀 Características

- ✅ Carga automática de datasets desde archivos ZIP
- ✅ Preprocesamiento de imágenes (RGB, redimensionamiento, normalización)
- ✅ Extracción de ground truth desde archivos MATLAB (.mat)
- ✅ División automática en conjuntos de entrenamiento, validación y test
- ✅ Implementación de arquitectura U-Net para detección de bordes
- ✅ Visualización de resultados y métricas

## 📁 Estructura del Proyecto

```
Image Dataset Explorer and Preprocessing with Python/
├── README.md                           # Este archivo
├── requirements.txt                    # Dependencias del proyecto
├── .gitignore                         # Archivos a ignorar por Git
├── notebooks/                         # Jupyter notebooks
│   └── assignment_final.ipynb         # Notebook principal
├── data/                              # Datos del proyecto (no incluido en Git)
│   └── Assignment data.zip            # Dataset original
└── docs/                              # Documentación adicional
    └── project_description.md         # Descripción detallada del proyecto
```

## 🛠️ Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/image-dataset-explorer.git
   cd image-dataset-explorer
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Descarga el dataset:**
   - Coloca el archivo `Assignment data.zip` en la carpeta `data/`
   - O sigue las instrucciones en el notebook para descargar desde tu ubicación

## 📊 Uso

1. **Abre el notebook principal:**
   ```bash
   jupyter notebook notebooks/assignment_final.ipynb
   ```

2. **Ejecuta las celdas en orden:**
   - Importación y descompresión de datos
   - Definición de rutas
   - Preprocesamiento y carga del dataset
   - Configuración de la arquitectura U-Net
   - Entrenamiento y evaluación

## 📦 Dependencias

Las principales dependencias incluyen:

- `tensorflow` - Framework de deep learning
- `numpy` - Computación numérica
- `matplotlib` - Visualización
- `PIL` - Procesamiento de imágenes
- `scipy` - Carga de archivos .mat
- `jupyter` - Notebooks interactivos

Ver `requirements.txt` para la lista completa.

## 📈 Resultados

El proyecto procesa un dataset de imágenes con la siguiente estructura:
- **Entrenamiento**: 200 imágenes (256x256x3)
- **Validación**: 100 imágenes (256x256x3)  
- **Test**: 200 imágenes (256x256x3)

Cada imagen tiene su correspondiente máscara de bordes (256x256x1) extraída de archivos .mat.

