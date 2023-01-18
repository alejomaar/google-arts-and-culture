# Google Art & Culture Image Classification

### Problem description

La pagina Google Art and Culture es un repositorio de obras artisticas, en diferentes momentos del tiempo,cada pintura de estas posee atributos, como su localizacion, fecha de creacion. La variable de interes en este caso fue el color de cada obra entre las cuales se encuentran:

- Rojo - Verde - Azul - negro - Blanco

Este proyecto es multiproposito, y en general busca como generar un proyecto de data desde 0. Pasando desde el webscraping de imagenes, analisis, extraccion de caracterisitcas, construir modelo de supervisado de clasificacion y finalmente construccion de miscroservicio y despliege en AWS.

### Resultados

- Se extrayeron 18000 imagenes con procesamiento paralelo
- Extraer un vector de 18 caracteristicas por cada imagen.
- EDA de las catacteristicas de cada categoria
- Modelo SVM 88% de accuracy, incluye(Model selection, hyperparameter tunning, feature importance and export model.)
- Create and Containerizer a FastAPI app for serving ML model (Load a image and classifiy its color)
- Deploy to cloud

### Tecnologies

- `webscraping`: Python (Pandas, Selenium, Multiprocessing), Javascript.
- `eda`: Python (Pandas, matplotlib, seaborn)
- `feature extraction`: Python (Opencv,Numpy)
- `models`: Sklearn including logistic Regression,SVM, Random Forest
- `deploy`: Python (FastAPI) Docker,AWS

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
