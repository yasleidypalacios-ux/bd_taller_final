# Taller Final — APIs Públicas, MongoDB y EDA
**Curso:** Bases de Datos 
## Descripción
extracción de datos desde una API pública, almacenamiento
en MongoDB Atlas y análisis exploratorio de datos (EDA).

## API Usada
**REST Countries** (restcountries.com)  
Provee información de 250 países: nombre, región, población,
área, capital e idiomas.

## Prerrequisitos
- Python 3.10+
- MongoDB 
- Librerías: `requests`, `pymongo`, `pandas`, `matplotlib`, `seaborn`, `jupyter`

## Estructura del Proyecto
- `ingesta.py` — Script de extracción y carga a MongoDB
- `analisis.ipynb` — Notebook con el EDA completo
- `requirements.txt` — Librerías necesarias
- `.gitignore` — Archivos excluidos del repositorio

## Cómo Ejecutarlo
1. Clonar el repositorio
2. Crear entorno virtual: `py -m venv venv`
3. Activarlo: `venv\Scripts\activate`
4. Instalar librerías: `pip install -r requirements.txt`
5. Correr ingesta: `py ingesta.py`
6. Abrir notebook: `jupyter notebook`

## Resultados del EDA
- 250 países analizados
- El país más poblado es India con 1,417,492,000 habitantes
- El país más grande es Rusia con 17,098,246 km²
- África es la región con más países (59)
- Promedio de idiomas oficiales por país: 1.66
- Población total registrada: 8,019,495,460 habitantes
