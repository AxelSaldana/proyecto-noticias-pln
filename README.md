# 📰 Proyecto PLN - Procesamiento de Lenguaje Natural en Noticias

## 🎓 Información Académica

**Universidad:** Universidad Politécnica de San Luis Potosí  
**Materia:** Inteligencia Artificial 2  
**Profesor:** Manuel Chávez Pérez  

### 👥 Equipo de Desarrollo
- **Emiliano Chequer Enriquez** - 180016
- **Jorge Matadamas Cortes** - 180789  
- **Axel Rivera Saldaña** - 180606

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de **Procesamiento de Lenguaje Natural (PLN)** para extraer, analizar y procesar noticias del sitio web [El Pulso SLP](https://pulsoslp.com.mx/). El sistema permite:

- ✅ Extracción automática de noticias y títulos
- ✅ Procesamiento de texto con tokenización y stemming
- ✅ Búsqueda de palabras clave en las noticias
- ✅ Análisis de relevancia usando TF-IDF
- ✅ Generación de índices de palabras
- ✅ Almacenamiento de noticias en archivos de texto

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **BeautifulSoup4** - Web scraping
- **Requests** - Peticiones HTTP
- **NLTK** - Procesamiento de lenguaje natural
- **Pandas** - Manipulación de datos
- **NumPy** - Operaciones numéricas
- **Scikit-learn** - Machine learning y TF-IDF
- **Sentence-splitter** - Segmentación de oraciones

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/proyecto-noticias-pln.git
cd proyecto-noticias-pln
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Descargar recursos de NLTK
```python
import nltk
nltk.download('punkt')
```

## 🚀 Uso del Sistema

### Ejecución Principal
```bash
python procesador_noticias.py
```

### Uso Programático
```python
from procesador_noticias import ProcesadorNoticias

# Crear instancia del procesador
procesador = ProcesadorNoticias()

# Obtener noticias
procesador.obtener_noticias()
procesador.extraer_contenido_noticias()

# Guardar en archivos
procesador.guardar_noticias_txt()

# Crear índice para búsquedas
procesador.crear_indice()

# Buscar palabra específica
procesador.buscar_palabra("política")

# Análisis de relevancia
procesador.analizar_relevancia_tfidf("economía", top_n=5)
```

## 📁 Estructura del Proyecto

```
proyecto-noticias-pln/
├── README.md                           # Este archivo
├── requirements.txt                    # Dependencias del proyecto
├── procesador_noticias.py             # Código principal limpio y organizado
├── main.py                            # Código original del notebook
├── ProyectoFinalNoticias.ipynb        # Notebook original de Colab
└── noticias/                          # Directorio donde se guardan las noticias
    ├── noticia1.txt
    ├── noticia2.txt
    └── ...
```

## 🔍 Funcionalidades Principales

### 1. Extracción de Noticias
- Conexión automática al sitio web de El Pulso SLP
- Extracción de títulos y enlaces de noticias
- Descarga del contenido completo de cada noticia

### 2. Procesamiento de Texto
- **Tokenización:** Separación del texto en palabras individuales
- **Limpieza:** Eliminación de signos de puntuación
- **Normalización:** Conversión a minúsculas
- **Stemming:** Reducción de palabras a su raíz

### 3. Sistema de Búsqueda
- Creación de índice invertido para búsquedas rápidas
- Búsqueda de palabras clave en todas las noticias
- Identificación de archivos que contienen términos específicos

### 4. Análisis TF-IDF
- Cálculo de relevancia de términos por documento
- Ranking de noticias más relevantes para una palabra clave
- Análisis estadístico de frecuencia de términos

## 📊 Ejemplo de Salida

```
=== NOTICIAS EXTRAÍDAS ===
1. Gobierno de SLP anuncia nuevas medidas económicas
2. Universidad Politécnica inaugura nuevo laboratorio
3. Sector turístico muestra signos de recuperación
...

=== BÚSQUEDA DE PALABRAS ===
Ingresa una palabra para buscar: universidad

La palabra 'universidad' se encontró en:
  - Universidad_Politecnica_inaugura_nuevo_laboratorio_2.txt
  - Convenio_educativo_universidades_5.txt

TOP 5 archivos más relevantes para 'universidad':
1. Universidad_Politecnica_inaugura_nuevo_laboratorio_2 (Score: 0.8542)
2. Convenio_educativo_universidades_5 (Score: 0.6234)
...
```

## 🤝 Contribuciones

Este proyecto fue desarrollado como parte del curso de Inteligencia Artificial 2. Las contribuciones están limitadas a los miembros del equipo de desarrollo.

## 📄 Licencia

Este proyecto es de uso académico y está desarrollado con fines educativos para la Universidad Politécnica de San Luis Potosí.

## 📞 Contacto

Para preguntas sobre este proyecto, contactar a cualquiera de los miembros del equipo de desarrollo mencionados anteriormente.

---

**Nota:** Este proyecto utiliza web scraping del sitio El Pulso SLP con fines académicos y de investigación. Se respetan los términos de uso del sitio web.
