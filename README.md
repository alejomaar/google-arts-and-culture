# Google Art & Culture Image Classification

## 1) Problem description

The Google Art and Culture page is a repository of artistic works, at different moments in time, each painting has attributes, such as its location, date of creation. The variable of interest in this case was the color of each work, among which are:

`BLACK` `BROWN` `TEAL` `GREEN` `BLUE` `WHITE` `RED` `YELLOW` `ORANGE` `PURPLE` `PINK`

This project is multipurpose, and in general it seeks how to generate a data project from scratch. Going from image webscraping, analysis, feature extraction, building a classification supervised model and finally building a microservice.

### 2) Results

#### Webscraping

- Scraping 16311 images using multiprocessing in python

#### Feature Extraction

- Extract a vector of 18 features for each image. The characteristics are based on the average and std of image in the color channels (RGB,HSV,LAB)

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

- Select the best model (SVM with a 87.8% +-0.2% of accuracy)
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
│ │ ├── img_classify.py <- Processing the image to classify by color.
│ └── utility <- Utility functions
│ │ ├── conversion.py <- Convert raw bytes into a opencv/numpy image
├── data
│ ├── external <- Data from third party
│ ├── interim <- Intermediate data that has been transformed.
│ │ └── pictures.csv
│ ├── processed <- The final, canonical data sets for modeling.
│ │ ├── img
│ │ └── pictures.csv <- Final dataset.
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

### 3) Installation

- Prerequisites
  In order to manage the dependencies of the project you could:

* `pip install pipenv`
* Have `docker` in your computer

- Steps

1. Run: `pipenv install`
2. Run: `pipenv shell`
3. Run: `docker build -t google-images-classifier .`

### 4) Use this project

- If you want see the scraping, analysis and model selection process:
  Check `notebooks` folder

- If you want retrain the model:
  Run `python -m src.models.train_model`

- If you want run server

  1. Run `uvicorn main:app --host 0.0.0.0 --port 9797 --reload`
  2. Check the docs in `http://localhost:9797/docs`

- If you want run the container
  1. Run: `docker run -it -p 9797:9797 google-images-classifier`
  2. Check the docs in `http://localhost:9797/docs`
