import pyprojroot
from joblib import load

# Constants
root_path =  pyprojroot.here()
models_path = (root_path / "models/svm_classifier.joblib")

svm_model = load(models_path)

input = {'b_bgr_mean': 0.9218758706116625,
 'g_bgr_mean': -0.24277016711618238,
 'r_bgr_mean': -1.8562252992889867,
 'h_hsv_mean': 2.051317157021624,
 's_hsv_mean': 2.774457885985387,
 'v_hsv_mean': 0.27577374353112716,
 'l_lab_mean': -0.31071535947737555,
 'a_lab_mean': -0.550672487967333,
 'b_lab_mean': -2.888146382899049,
 'b_bgr_std': -0.33184172259240213,
 'g_bgr_std': -0.5823828753642223,
 'r_bgr_std': -0.265741111893936,
 'h_hsv_std': -0.5971872072191281,
 's_hsv_std': 0.10909976358637759,
 'v_hsv_std': -0.9927300623621939,
 'l_lab_std': -0.9497327744654422,
 'a_lab_std': 1.7573013668773538,
 'b_lab_std': 1.187729057355215}

x =  list(input.values())
X = [x]
y_pred = svm_model.predict(X)

print(y_pred)