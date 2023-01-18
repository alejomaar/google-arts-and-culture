# google-art-and-culture

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
