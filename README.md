# Google Art & Culture Image Classification

### Problem description

La pagina Google Art and Culture es un repositorio de obras artisticas, en diferentes momentos del tiempo,cada pintura de estas posee atributos, como su localizacion, fecha de creacion. La variable de interes en este caso fue el color de cada obra entre las cuales se encuentran:

- Rojo - Verde - Azul - negro - Blanco

Este proyecto es multiproposito, y en general busca como generar un proyecto de data desde 0. Pasando desde el webscraping de imagenes, analisis, extraccion de caracterisitcas, construir modelo de supervisado de clasificacion y finalmente construccion de miscroservicio y despliege en AWS.

### Resultados

#### Webscraping

- Scrape 18000 images using multiprocessing in python

#### Feature Extraction

- Extract a vector of 18 characteristics for each image. The characteristics compose the mean and td of image in the color channels (RGB,HSV,LAB)

#### EDA

- Perform some visualization about the features and the target variable.
- Check similarities and differences between the features.
- Verify if dataset is imbalanced

#### Model Selection

- Feature Scaling (Standard Scaling)
- Try different models including hyperparameter tuning and cross validation (SVM, Logistic Regression)

| params                                 | mean_test_accuracy | std_test_score |          classifier |
| :------------------------------------- | :----------------: | :------------: | ------------------: |
| { 'C': 100, 'gamma': 0.01}             |       0.878        |     0.002      |                 svm |
| {' alpha': 1, 'hidden...': 400, ...}   |       0.874        |     0.004      |      neural_network |
| {'C': 15}                              |       0.862        |     0.004      | logistic_regression |
| {'max_depth': 25, 'n_estimators': 170} |       0.836        |     0.006      |       random_forest |
| {'max_depth': 100, 'n_estimators': 50} |       0.782        |     0.006      |   gradient_boosting |

- Select the best model (SVM with a 88% +-0.2% of accuracy)
- Feature Importance (Top 5)

  | feature    | importance |
  | :--------- | ---------: |
  | b_lab_mean |   0.277048 |
  | a_lab_mean |   0.256891 |
  | s_hsv_mean |   0.172290 |
  | a_lab_std  |   0.131976 |
  | v_hsv_mean |   0.130603 |
  | r_bgr_mean |   0.092692 |

`Note`: HSV and LAB color spaces looks be the most important features for classifing the color of a image

- Confusion Matrix

[confusion_matrix](references/confusion_matrix.png)

`Note 1`: Purple,Blue and Teal colors tends to be the highest errors. However, this color are similiar, so, this mismatch classifications in not so bad.
`Note 2`: Classify Pink is actualy the worst class (79.2%) tends to confuse with differents classes.
`Note 3`: White and Black are the most accurate classes. Maybe because this are neutral colors and concecuently more easy for machine classfication.

#### Deploy

- Export best model and scaler as .joblib file (Check models folder)
- Conteineraize app with Docker (More details in `Instalation Section`)
- Use FastAPI for serve models as microservice
- Deploy to AWS Beanstalk.

### Tecnologies

- `webscraping`: Python (Pandas, Selenium, Multiprocessing), Javascript.
- `eda`: Python (Pandas, matplotlib, seaborn)
- `feature extraction`: Python (Opencv,Numpy)
- `models`: Sklearn including logistic Regression,SVM, Random Forest
- `deploy`: Python (FastAPI), Docker,AWS

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
