# Google Art & Culture Image Classification

### Problem description

Este proyecto busca raspar las pinturas artisticas en la pagina de Google Art / Culture
para posteriormente ingresarlas en un algoritmo de clasificacion. Cada una de estas pinturas tiene varios metadatos; el color es la variable objetivo. dentro de los cuales encontramos algunas categorias.

- Rojo - Verde - Azul - negro - Blanco

El proposito general de este proyecto es, como desde 0, se pueden extraer imagenes de una pagina web, categorizarlas, extraer caracteristicas de ellas y finalmente contruir un modelo de ML que pueda clasificarlas. Este proyecto tomado como un microservicio escalable de ML , con su entorno virtual, dockerizado y desplegado en la nube.

### Resultados

- Se extrayeron 18000 imagenes con procesamiento paralelo
- Extraer un vector de 18 caracteristicas por cada imagen.
- EDA de las catacteristicas de cada categoria
- Model selection, hyperparameter tunning, feature importance and export model.
- Create and Containerizer a FastAPI app for serving ML model (Load a image and classifiy its color)
- Deploy to cloud

### Tecnologies

- `webscraping`: Python (Pandas, Selenium, Multiprocessing), Javascript.
- `eda`: Python (Pandas, matplotlib, seaborn)
- `models`: Python (Sklearn,opencv,numpy)
- `deploy`: Python (FastAPI,OpenCV) Docker,AWS

#Folder structure

```bash
├── application
│ ├── routers <- Separate API into routers
│ │ ├── classify.py <- API for image classification
│ ├── services <- Business logic
│ │ ├── img_classify.py <- Processing image for classify it color
│ └── utility <- Utility functions
│ │ ├── conversion.py <- Convert raw bytes into a opencv/numpy image
├── data
│ ├── external <- Data from third party
│ ├── interim <- Intermediate data that has been transformed.
│ │ └── pictures.csv
│ ├── processed <- The final, canonical data sets for modeling.
│ │ ├── img
│ │ └── pictures.csv
│ └── raw <- The original, immutable data dump.
├── dockerfile <- file for build docker image
├── LICENSE
├── main.py <- Service entry point
├── models <- Trained and serialized models, model predictions, or model summaries
│ ├── scaler.joblib <- Feature Scaler
│ └── svm_classifier.joblib <- Image Classifier
├── notebooks <- Jupyter notebooks. Naming convention is a number (for ordering)
│ ├── 01-scraping.ipynb <- Scraping Data & images
│ ├── 02-features.ipynb <- Feature Extraction from raw images
│ ├── 03-eda.ipynb <- EDA
│ └── 04-models.ipynb <- Build different models
├── Pipfile <- Virtual Environment file
├── Pipfile.lock <- Virtual Environment file
├── README.md <- The top-level README for developers
├── references <- Data dictionaries, manuals, and all other explanatory materials
│ └── picture.jpg
├── requirements.txt <- The requirements file for reproducing packages used in this project
├── setup.py <- makes project pip installable (pip install -e .) so src can be imported
├── src
│ ├── features <- Scripts to turn raw data into features for modeling
│ │ ├── extract_features.py
│ ├── models <- Scripts to train models and then use trained models to make
│ │ ├── predict_model.py
│ │ └── train_model.py
│ ├── scraping <- Scripts for scraping images and data
│ │ ├── get_img.py
│ │ ├── scraping_pictures.py
│ │ └── scripts.py
│ ├── visualization <- Scripts to create exploratory and results oriented visualizations
│ │ ├── imgshow.py

```
