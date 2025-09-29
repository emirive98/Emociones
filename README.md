# 🌙 Emotions Dashboard  

## 🇪🇸 Descripción en Español
Un proyecto en **Python + Streamlit** que analiza y visualiza emociones a partir de un diario personal.  
El usuario escribe cómo se siente, el sistema detecta el sentimiento (positivo, negativo o neutro) y lo guarda en una base de datos.  
Luego muestra un **dashboard interactivo** con gráficos y estadísticas de la evolución emocional.  

---

### 🚀 Funcionalidades
- ✍️ **Input diario**: escribí cómo te sentís hoy.  
- 🤖 **Análisis automático** con TextBlob (positivo, negativo, neutro).  
- 💾 **Almacenamiento** en SQLite (`emociones.db`) y respaldo en CSV.  
- 📊 **Dashboard visual**:  
  - Gráfico de barras con distribución de emociones.  
  - Línea temporal con la evolución día a día.  
  - Nube de palabras con los términos más usados.  
- 🌑 **Modo oscuro y colores emocionales**:  
  - Verde → positivo  
  - Rojo → negativo  
  - Azul → neutro  

---

## 🇬🇧 English Description
A project built with **Python + Streamlit** to analyze and visualize emotions through personal journaling.  
The user writes how they feel, the system performs sentiment analysis (positive, negative, neutral), stores the entry in a database, and displays an **interactive dashboard** with emotional trends and stats.  

---

### 🚀 Features
- ✍️ **Daily input**: write how you feel today.  
- 🤖 **Automatic sentiment analysis** with TextBlob (positive, negative, neutral).  
- 💾 **Storage** in SQLite (`emociones.db`) and optional CSV backup.  
- 📊 **Dashboard visualizations**:  
  - Bar chart with emotion distribution.  
  - Time series line chart showing emotional evolution.  
  - Word cloud with the most frequent words.  
- 🌑 **Dark mode and emotional colors**:  
  - Green → positive  
  - Red → negative  
  - Blue → neutral  

---

## 📦 Instalación / Installation
Clonar el repositorio / Clone the repository:
- bash
git clone https://github.com/TU_USUARIO/emotions-dashboard.git
cd emotions-dashboard

--------------------------------------
pip install -r requirements.txt
python -m textblob.download_corpora
--------------------------------------
Ejecutar la aplicación con Streamlit / Run the app with Streamlit:
streamlit run dashboard_emociones.py


Siéntete libre de hacer journaling y mejorar tu vida 💜

Te manda saludos, Emi Rivera

Feel free to start journaling and improve your life 💜

Greetings from, Emi Rivera 
