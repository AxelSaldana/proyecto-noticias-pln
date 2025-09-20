# 📰 News NLP Processor - Natural Language Processing for News Articles

## 🎓 Academic Information

**University:** Universidad Politécnica de San Luis Potosí  
**Course:** Artificial Intelligence 2  
**Professor:** Manuel Chávez Pérez  

### 👥 Development Team
- **Emiliano Chequer Enriquez** - 180016
- **Jorge Matadamas Cortes** - 180789  
- **Axel Rivera Saldaña** - 180606

## 📋 Project Description

This project implements a **Natural Language Processing (NLP)** system to extract, analyze, and process news articles from the [El Pulso SLP](https://pulsoslp.com.mx/) website. The system provides:

- ✅ Automatic news and title extraction
- ✅ Text processing with tokenization and stemming
- ✅ Keyword search in news articles
- ✅ Relevance analysis using TF-IDF
- ✅ Word index generation
- ✅ News storage in text files

## 🛠️ Technologies Used

- **Python 3.8+**
- **BeautifulSoup4** - Web scraping
- **Requests** - HTTP requests
- **NLTK** - Natural language processing
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Scikit-learn** - Machine learning and TF-IDF
- **Sentence-splitter** - Sentence segmentation

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/AxelSaldana/news-nlp-processor.git
cd news-nlp-processor
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download NLTK resources
```python
import nltk
nltk.download('punkt')
```

## 🚀 System Usage

### Main Execution
```bash
python procesador_noticias.py
```

### Programmatic Usage
```python
from procesador_noticias import ProcesadorNoticias

# Create processor instance
procesador = ProcesadorNoticias()

# Get news
procesador.obtener_noticias()
procesador.extraer_contenido_noticias()

# Save to files
procesador.guardar_noticias_txt()

# Create index for searches
procesador.crear_indice()

# Search for specific word
procesador.buscar_palabra("política")

# Relevance analysis
procesador.analizar_relevancia_tfidf("economía", top_n=5)
```

## 📁 Project Structure

```
news-nlp-processor/
├── README.md                           # This file
├── requirements.txt                    # Project dependencies
├── procesador_noticias.py             # Main clean and organized code
├── main.py                            # Original notebook code
├── ProyectoFinalNoticias.ipynb        # Original Colab notebook
└── noticias/                          # Directory where news are saved
    ├── noticia1.txt
    ├── noticia2.txt
    └── ...
```

## 🔍 Main Features

### 1. News Extraction
- Automatic connection to El Pulso SLP website
- Extraction of news titles and links
- Download of complete content for each news article

### 2. Text Processing
- **Tokenization:** Text separation into individual words
- **Cleaning:** Removal of punctuation marks
- **Normalization:** Conversion to lowercase
- **Stemming:** Word reduction to their root form

### 3. Search System
- Creation of inverted index for fast searches
- Keyword search across all news articles
- Identification of files containing specific terms

### 4. TF-IDF Analysis
- Calculation of term relevance per document
- Ranking of most relevant news for a keyword
- Statistical analysis of term frequency

## 📊 Example Output

```
=== EXTRACTED NEWS ===
1. SLP Government announces new economic measures
2. Polytechnic University inaugurates new laboratory
3. Tourism sector shows signs of recovery
...

=== WORD SEARCH ===
Enter a word to search: university

The word 'university' was found in:
  - Universidad_Politecnica_inaugura_nuevo_laboratorio_2.txt
  - Convenio_educativo_universidades_5.txt

TOP 5 most relevant files for 'university':
1. Universidad_Politecnica_inaugura_nuevo_laboratorio_2 (Score: 0.8542)
2. Convenio_educativo_universidades_5 (Score: 0.6234)
...
```

## 🤝 Contributions

This project was developed as part of the Artificial Intelligence 2 course. Contributions are limited to the development team members.

## 📄 License

This project is for academic use and developed for educational purposes at Universidad Politécnica de San Luis Potosí.

## 📞 Contact

For questions about this project, contact any of the development team members mentioned above.

---

**Note:** This project uses web scraping from El Pulso SLP website for academic and research purposes. The website's terms of use are respected.
