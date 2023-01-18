# google-art-and-culture

├── application
│ ├── routers <- Separate API into routers
│ │ ├── classify.py <- API for image classification
│ ├── services <- Business logic
│ │ ├── img_classify.py <- Processing image for classify it color
│ └── utility <-
│ │ ├── conversion.py
├── build
│ ├── bdist.linux-x86_64
│ └── lib
│ └── src
├── data
│ ├── external
│ ├── interim
│ │ └── pictures.csv
│ ├── processed
│ │ ├── img
│ │ └── pictures.csv
│ └── raw
├── dockerfile
├── LICENSE
├── main.py
├── models
│ ├── scaler.joblib
│ └── svm_classifier.joblib
├── notebooks
│ ├── 01-scraping.ipynb
│ ├── 02-features.ipynb
│ ├── 03-eda.ipynb
│ └── 04-models.ipynb
├── Pipfile
├── Pipfile.lock
├── **pycache**
│ └── main.cpython-39.pyc
├── README.md
├── references
│ └── picture.jpg
├── reports
│ └── figures
├── requirements.txt
├── setup.py
├── src
│ ├── features
│ │ ├── extract_features.py
│ │ └── **init**.py
│ ├── **init**.py
│ ├── models
│ │ ├── **init**.py
│ │ ├── predict_model.py
│ │ └── train_model.py
│ ├── scraping
│ │ ├── get_img.py
│ │ ├── **init**.py
│ │ ├── scraping_pictures.py
│ │ └── scripts.py
│ └── visualization
│ ├── imgshow.py
│ └── **init**.py
└── src.egg-info
├── dependency_links.txt
├── PKG-INFO
├── SOURCES.txt
└── top_level.txt

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
