# Descripción Detallada del Proyecto

## 🎯 Objetivo

Este proyecto implementa un sistema completo para la exploración y preprocesamiento de datasets de imágenes, específicamente diseñado para tareas de **detección de bordes (edge detection)** utilizando redes neuronales convolucionales.

## 📊 Dataset

El proyecto trabaja con un dataset estructurado que contiene:

### Estructura de Datos
```
Assignment data/
├── data/
│   ├── images/
│   │   ├── train/     # 200 imágenes de entrenamiento
│   │   ├── val/       # 100 imágenes de validación
│   │   └── test/      # 200 imágenes de test
│   └── groundTruth/
│       ├── train/     # 200 archivos .mat de ground truth
│       ├── val/       # 100 archivos .mat de ground truth
│       └── test/      # 200 archivos .mat de ground truth
```

### Formato de Datos
- **Imágenes**: Archivos JPG en formato RGB
- **Ground Truth**: Archivos MATLAB (.mat) conteniendo información de bordes
- **Tamaño**: Imágenes redimensionadas a 256x256 píxeles
- **Normalización**: Valores de píxeles normalizados a [0,1]

## 🔧 Funcionalidades Implementadas

### 1. Preprocesamiento de Imágenes
```python
def preprocess_image(image_path, size=(256, 256)):
    """
    - Carga imagen en formato RGB
    - Redimensiona a tamaño especificado
    - Normaliza valores a [0,1]
    - Retorna array NumPy (h, w, 3)
    """
```

### 2. Procesamiento de Ground Truth
```python
def preprocess_boundary(gt_path, size=(256, 256), threshold=0.5):
    """
    - Carga archivo .mat
    - Extrae información de 'Boundaries'
    - Redimensiona usando interpolación bilineal
    - Binariza usando umbral especificado
    - Retorna máscara binaria (0 o 1)
    """
```

### 3. Carga de Dataset
```python
def load_dataset(img_dir, gt_dir, size=(256,256), threshold=0.5):
    """
    - Itera sobre todas las imágenes y archivos .mat
    - Aplica preprocesamiento a ambos
    - Retorna arrays NumPy X (imágenes) y Y (máscaras)
    """
```

### 4. Arquitectura U-Net
El proyecto implementa una arquitectura U-Net para detección de bordes:

- **Encoder**: Extracción de características progresiva
- **Decoder**: Reconstrucción de características con skip connections
- **Output**: Mapa de probabilidades de bordes (256x256x1)

## 📈 Métricas y Evaluación

### Métricas Implementadas
- **Precision**: Exactitud de las predicciones positivas
- **Recall**: Sensibilidad de detección de bordes
- **F1-Score**: Media armónica de precision y recall
- **IoU (Intersection over Union)**: Solapamiento entre predicción y ground truth

### Visualización
- Comparación lado a lado de imágenes originales, ground truth y predicciones
- Gráficos de métricas durante el entrenamiento
- Análisis de ejemplos específicos

## 🚀 Uso del Sistema

### Configuración Inicial
1. **Descompresión**: El sistema automáticamente descomprime el archivo ZIP
2. **Definición de Rutas**: Configuración automática de rutas para cada conjunto de datos
3. **Preprocesamiento**: Carga y preparación de todos los datos

### Entrenamiento
```python
# Configuración del modelo
model = create_unet_model(input_shape=(256, 256, 3))

# Compilación
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', 'precision', 'recall']
)

# Entrenamiento
history = model.fit(
    X_train, Y_train,
    validation_data=(X_val, Y_val),
    epochs=50,
    batch_size=32
)
```

### Evaluación
```python
# Evaluación en conjunto de test
test_loss, test_accuracy, test_precision, test_recall = model.evaluate(X_test, Y_test)

# Predicciones
predictions = model.predict(X_test)
```

## 🔍 Análisis Exploratorio

El proyecto incluye análisis detallado del dataset:

### Estadísticas Básicas
- Número de imágenes por conjunto
- Distribución de tamaños de imagen
- Análisis de valores de píxeles

### Visualización de Datos
- Muestras aleatorias de imágenes
- Correspondencia entre imágenes y ground truth
- Análisis de distribución de bordes

## 🛠️ Tecnologías Utilizadas

### Librerías Principales
- **TensorFlow/Keras**: Framework de deep learning
- **NumPy**: Computación numérica
- **Matplotlib/Seaborn**: Visualización
- **PIL (Pillow)**: Procesamiento de imágenes
- **SciPy**: Carga de archivos MATLAB

### Herramientas de Desarrollo
- **Jupyter Notebook**: Entorno de desarrollo interactivo
- **Git**: Control de versiones
- **Python 3.8+**: Lenguaje de programación

## 📋 Requisitos del Sistema

### Hardware Recomendado
- **RAM**: Mínimo 8GB, recomendado 16GB+
- **GPU**: Opcional pero recomendado para entrenamiento más rápido
- **Almacenamiento**: 2GB+ para dataset y modelos

### Software
- **Python**: 3.8 o superior
- **CUDA**: Opcional para aceleración GPU
- **Jupyter**: Para notebooks interactivos

## 🔮 Extensiones Futuras

### Mejoras Propuestas
1. **Data Augmentation**: Rotación, zoom, flip para aumentar dataset
2. **Transfer Learning**: Uso de modelos pre-entrenados
3. **Ensemble Methods**: Combinación de múltiples modelos
4. **Real-time Processing**: Pipeline para procesamiento en tiempo real
5. **API REST**: Interfaz web para predicciones

### Optimizaciones
- **Mixed Precision**: Entrenamiento más rápido con menor memoria
- **Distributed Training**: Entrenamiento en múltiples GPUs
- **Model Compression**: Reducción de tamaño del modelo
- **Quantization**: Optimización para inferencia

## 📚 Referencias

- **U-Net Paper**: "U-Net: Convolutional Networks for Biomedical Image Segmentation"
- **TensorFlow Documentation**: Guías oficiales de implementación
- **Edge Detection**: Fundamentos teóricos de detección de bordes
- **Image Processing**: Técnicas de preprocesamiento de imágenes

---

*Este documento proporciona una descripción completa del proyecto para facilitar su comprensión y uso.*
