import pandas as pd
from joblib import dump
import pyprojroot
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Constants
root_path =  pyprojroot.here()
data_processed_folder = (root_path / "data"/'processed')
models_folder = (root_path / "models")

feature_columns = ['b_bgr_mean','g_bgr_mean','r_bgr_mean','h_hsv_mean','s_hsv_mean',\
'v_hsv_mean','l_lab_mean','a_lab_mean','b_lab_mean','b_bgr_std','g_bgr_std','r_bgr_std',\
'h_hsv_std','s_hsv_std','v_hsv_std','l_lab_std','a_lab_std','b_lab_std'
]

target_column = 'color'

#Functions
def get_dataframe():
    return  pd.read_csv(data_processed_folder/'pictures.csv')

def prepare_data(df):
    X = df[feature_columns]
    y = df[target_column].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    dump(scaler, models_folder/'scaler.joblib')
    return X,y

def train(X,y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0,stratify=y)

    svm_model = SVC(random_state=1,C=100,gamma=0.01)
    svm_model.fit(x_train,y_train)
    score = svm_model.score(x_test,y_test)
    print('{:2f}'.format(score))
    dump(svm_model, models_folder/'svm_classifier.joblib')
    print('Finish train')

#Read Data
df =  get_dataframe()
# Separate X and Y 
X,y = prepare_data(df)
# Train model
train(X,y)
