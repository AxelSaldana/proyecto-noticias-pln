# -*- coding: utf-8 -*-
"""
PROYECTO PLN - Procesamiento de Lenguaje Natural en Noticias
Universidad Politécnica de San Luis Potosí
Inteligencia Artificial 2

Profesor:
    Manuel Chávez Pérez

Alumnos:
    Emiliano Chequer Enriquez 180016
    Jorge Matadamas Cortes 180789
    Axel Rivera Saldaña 180606
"""

# Importaciones
from bs4 import BeautifulSoup as soup
import requests
import os
import random
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sentence_splitter import SentenceSplitter
import collections
from nltk.probability import ConditionalFreqDist

class ProcesadorNoticias:
    """Clase para procesar noticias de El Pulso SLP"""
    
    def __init__(self):
        self.url_base = "https://pulsoslp.com.mx/"
        self.titulos = []
        self.noticias = []
        self.links = []
        self.indice = {}
        self.splitter = SentenceSplitter(language='es')
        
        # Descargar recursos de NLTK si es necesario
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
    
    def obtener_noticias(self):
        """Extrae títulos y enlaces de noticias del sitio web"""
        print("Obteniendo noticias de El Pulso SLP...")
        
        # Realizar solicitud a la página principal
        r = requests.get(self.url_base)
        b = soup(r.content, 'lxml')
        
        # Extraer títulos
        for news in b.findAll('h2'):
            self.titulos.append(news.text.strip())
        
        # Extraer enlaces
        for news in b.findAll('h2', {'class': 'entry-title td-module-title'}):
            if news.a and news.a.get('href'):
                self.links.append(news.a['href'])
        
        print(f"Se encontraron {len(self.titulos)} títulos y {len(self.links)} enlaces")
        return self.titulos, self.links
    
    def extraer_contenido_noticias(self):
        """Extrae el contenido completo de cada noticia"""
        print("Extrayendo contenido de las noticias...")
        
        for link in self.links:
            try:
                page = requests.get(self.url_base + link)
                bsobj = soup(page.content, 'lxml')
                
                for news in bsobj.findAll('div', {'class': 'td-paragraph-padding-0'}):
                    self.noticias.append(news.text.strip())
                    break  # Solo tomar el primer párrafo principal
            except Exception as e:
                print(f"Error al procesar {link}: {e}")
                continue
        
        print(f"Se extrajeron {len(self.noticias)} noticias")
        return self.noticias
    
    def guardar_noticias_txt(self, directorio="noticias"):
        """Guarda las noticias en archivos de texto"""
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        
        print(f"Guardando noticias en directorio '{directorio}'...")
        
        for i, (titulo, noticia) in enumerate(zip(self.titulos, self.noticias), 1):
            # Limpiar el título para usarlo como nombre de archivo
            titulo_limpio = "".join(c for c in titulo if c.isalnum() or c in (' ', '-', '_')).rstrip()
            nombre_archivo = f"{titulo_limpio}_{i}.txt"
            
            try:
                with open(f"{directorio}/{nombre_archivo}", "w", encoding="utf-8") as f:
                    f.write(noticia)
            except Exception as e:
                print(f"Error al guardar {nombre_archivo}: {e}")
        
        print(f"Noticias guardadas en {directorio}/")
    
    def mostrar_titulos(self):
        """Muestra los títulos de las noticias extraídas"""
        print("\n=== NOTICIAS EXTRAÍDAS ===")
        for i, titulo in enumerate(self.titulos, 1):
            print(f"{i}. {titulo}")
        print()
    
    def tokenizar(self, texto):
        """Tokeniza el texto removiendo puntuación"""
        puntuacion = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~¿¡..'
        tokens = nltk.word_tokenize(texto, "spanish")
        
        for i, token in enumerate(tokens):
            tokens[i] = token.strip(puntuacion)
        
        texto = " ".join(tokens)
        tokens = nltk.word_tokenize(texto, "spanish")
        return [token for token in tokens if token]  # Remover tokens vacíos
    
    def stemmizar(self, tokens):
        """Aplica stemming a los tokens"""
        stemmer = nltk.stem.SnowballStemmer("spanish")
        return [stemmer.stem(token) for token in tokens]
    
    def crear_indice(self, directorio="noticias"):
        """Crea un índice de palabras por archivo"""
        print("Creando índice de palabras...")
        
        if not os.path.exists(directorio):
            print(f"El directorio {directorio} no existe")
            return
        
        archivos = os.listdir(directorio)
        
        for archivo in archivos:
            try:
                with open(f"{directorio}/{archivo}", "r", encoding="utf-8") as f:
                    texto = f.read().lower()
                    tokens = self.tokenizar(texto)
                    vocabulario = set(tokens)
                    
                    for palabra in vocabulario:
                        if palabra not in self.indice:
                            self.indice[palabra] = set()
                        self.indice[palabra].add(archivo)
            except Exception as e:
                print(f"Error al procesar {archivo}: {e}")
        
        print(f"Índice creado con {len(self.indice)} palabras únicas")
    
    def buscar_palabra(self, palabra):
        """Busca una palabra en el índice"""
        palabra = palabra.lower()
        
        if palabra in self.indice:
            print(f"La palabra '{palabra}' se encontró en:")
            for archivo in self.indice[palabra]:
                print(f"  - {archivo}")
            return self.indice[palabra]
        else:
            print(f"No se encontraron referencias para la palabra '{palabra}'")
            return set()
    
    def analizar_relevancia_tfidf(self, palabra, directorio="noticias", top_n=5):
        """Analiza la relevancia de una palabra usando TF-IDF"""
        if not os.path.exists(directorio):
            print(f"El directorio {directorio} no existe")
            return
        
        archivos = os.listdir(directorio)
        lista_archivos = [f"{directorio}/{archivo}" for archivo in archivos]
        
        try:
            vectorizador = TfidfVectorizer(
                input="filename",
                analyzer="word",
                sublinear_tf=True,
                encoding='utf-8'
            )
            
            matriz_tfidf = vectorizador.fit_transform(lista_archivos)
            vocabulario = vectorizador.get_feature_names_out()
            
            tabla_tfidf = pd.DataFrame(
                matriz_tfidf.toarray(),
                index=archivos,
                columns=vocabulario
            )
            
            if palabra.lower() in vocabulario:
                relevancia = tabla_tfidf[[palabra.lower()]].sum(axis=1).sort_values(ascending=False)
                
                print(f"\nTOP {top_n} archivos más relevantes para '{palabra}':")
                top_archivos = relevancia.head(top_n)
                
                for i, (archivo, score) in enumerate(top_archivos.items(), 1):
                    titulo_limpio = archivo.replace('.txt', '')
                    print(f"{i}. {titulo_limpio} (Score: {score:.4f})")
                
                return top_archivos
            else:
                print(f"La palabra '{palabra}' no se encontró en el vocabulario")
                return pd.Series()
                
        except Exception as e:
            print(f"Error en el análisis TF-IDF: {e}")
            return pd.Series()

def main():
    """Función principal"""
    procesador = ProcesadorNoticias()
    
    # 1. Obtener noticias
    procesador.obtener_noticias()
    
    # 2. Extraer contenido
    procesador.extraer_contenido_noticias()
    
    # 3. Guardar en archivos
    procesador.guardar_noticias_txt()
    
    # 4. Mostrar títulos
    procesador.mostrar_titulos()
    
    # 5. Crear índice
    procesador.crear_indice()
    
    # 6. Búsqueda interactiva
    while True:
        print("\n=== BÚSQUEDA DE PALABRAS ===")
        palabra = input("Ingresa una palabra para buscar (o 'salir' para terminar): ").strip()
        
        if palabra.lower() == 'salir':
            break
        
        if palabra:
            # Búsqueda simple
            procesador.buscar_palabra(palabra)
            
            # Análisis TF-IDF
            procesador.analizar_relevancia_tfidf(palabra)
    
    print("¡Gracias por usar el procesador de noticias!")

if __name__ == "__main__":
    main()
